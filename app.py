from flask import Flask, json, Response, request
from pifacecad.lcd import LCD_WIDTH
import pifacecad
import time

cad = pifacecad.PiFaceCAD()
switchlistener = pifacecad.SwitchEventListener(chip=cad)

app = Flask(__name__)
@app.route('/api', methods = ['POST'])
def api():
    if request.headers['Content-Type'] == 'application/json':
        content = request.get_json()
        cs.updateModel(content)

        resp = Response('', status=200, mimetype='application/json')
        return  resp

class CS():
    def __init__(self):
        self.current_index = 0
        self.model = []
        
    def updateModel(self,content):
        self.model = []
        self.model.append("Map: " + str(content['map']['name']))
        self.model.append("Player name: " + str(content['player']['name']))
        self.model.append("Player health: " + str(content['player']['state']['health']))

    def prevInformation(self,event=None):
        self.current_index = (self.current_index - 1) % len(self.model)
        cad.lcd.write(self.model[self.current_index])
        cad.lcd.clear()

    def nextInformation(self,event=None):
        self.current_index = (self.current_index + 1) % len(self.model)
        cad.lcd.write("{data}".format(
                              data=self.model[self.current_index]))

        time.sleep(2)
        cad.lcd.clear()
    
if __name__ == '__main__':
    cs = CS()
    cad.lcd.backlight_on()
    
    switchlistener.register(8, pifacecad.IODIR_ON, cs.prevInformation)
    switchlistener.register(7, pifacecad.IODIR_ON, cs.nextInformation)

    switchlistener.activate()

        
    app.run(host='0.0.0.0')
                                 


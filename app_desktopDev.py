from flask import Flask, json, Response, request
#from pifacecad.lcd import LCD_WIDTH
#import pifacecad
import time

#cad = pifacecad.PiFaceCAD()
#switchlistener = pifacecad.SwitchEventListener(chip=cad)

app = Flask(__name__)
@app.route('/api', methods = ['POST'])
def api():
    if request.headers['Content-Type'] == 'application/json':
        content = request.get_json(silent=True)
        cs.updateModel(content)

        resp = Response('', status=200, mimetype='application/json')
        return resp
    else:
        return 'Fail'

class CS():
    isBombPlanted = False

    def __init__(self):
        self.current_index = 0
        self.model = []
        
    def updateModel(self, content):
        self.model = []

        #player
        if content.get('player'):
            #team
            if content['player'].get('team'):
                if content['player']['team'] == 'T':
                    self.TerroLed()
                elif content['player']['team'] == 'CT':
                    self.CTLed()
            else:
                self.NoTeam()
            #name
            self.model.append("Player name: " + str(content['player'].get('name', 'Unknown')))
            #hp
            if content['player'].get('state'):
                self.model.append("Player health: " + str(content['player']['state'].get('health', 'Unknown')))
            #k/d
            if content['player'].get('match_stats'):    
                if content['player']['match_stats'].get('kills'):
                    k = float(content['player']['match_stats']['kills'])
                    if content['player']['match_stats'].get('deaths'):
                        d = float(content['player']['match_stats']['deaths'])
                        kd = k / d
                        self.model.append("K/D ratio: " + str(round(kd, 2)))
                    else:
                        self.model.append("K/D ratio: Perfect! " + str(k)[0]   + " kills")
    
        #map
        if content.get('map'):
            self.model.append("Map: " + str(content['map'].get('name', 'Unknown')))

        #bomb planted
        if content.get('added'):
            if content['added'].get('round'):
                if content['added']['round'].get('bomb') == True:
                    CS.isBombPlanted = True
                    self.bombPlanted()

        #bomb defused/exploded/ct killed
        if (content.get('round') == None or content['round'].get('bomb') == None or content['round']['bomb'] != 'planted') and CS.isBombPlanted == True:
            CS.isBombPlanted = False
            self.bombExplosion()

        print('\nModel:')
        print(self.model)

    def bombPlanted(self):
        print('---------- Planted! -----------')
        #TODO: burn the LED on plant!

    def bombExplosion(self):
        print('----------- Boom! -----------')
        #TODO: commit action on bomb exploded/defused/ct killed!
    
    def NoTeam(self):
        print('No team')
        #TODO: express being in no team

    def TerroLed(self):
        print('Team: T')
        #TODO: express being in T team

    def CTLed(self):
        print('Team: CT')
        #TODO: express being in CT team
'''
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
'''   
if __name__ == '__main__':
    cs = CS()
    '''
    cad.lcd.backlight_on()
    
    switchlistener.register(8, pifacecad.IODIR_ON, cs.prevInformation)
    switchlistener.register(7, pifacecad.IODIR_ON, cs.nextInformation)

    switchlistener.activate()
    ''' 
    app.run(host='127.0.0.1')
                                 


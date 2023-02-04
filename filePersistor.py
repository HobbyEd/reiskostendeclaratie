import json
import datetime
from ritPerMaand import ritPerMaand
from reisDag import reisDag
from rit import rit

class filePersistor(object):

    def getRitPerMaand(self, maand, jaar):
        self.__fileRitPerMaand = "./data/" + str(maand) + "_" + str(jaar) + "_ritpermaand.txt"
        with open(self.__fileRitPerMaand, 'r') as f:
            self.__ritPerMaandJSON = json.load(f)	
        self.__ritPerMaand = self.__maakRitPerMaandvanJSON(self.__ritPerMaandJSON)
        return self.__ritPerMaand


    def persisteerRitPerMaand(self, ritPerMaand):
        __fileRitPerMaand = "./data/" + str(ritPerMaand.getMaand()) + "_" + str(ritPerMaand.getJaar()) + "_ritpermaand.txt"
        file = open(__fileRitPerMaand, "w")
        file.write(self.__maakJSON(ritPerMaand))
        file.close()
        return True

    def __maakRitPerMaandvanJSON(self, ritPerMaandJSON):
        __ritPerMaand = ritPerMaand(int(ritPerMaandJSON['maand']), int(ritPerMaandJSON['jaar']))
        __ritPerMaand.zetTotaalAfstand(ritPerMaandJSON['totaalAfstand'])
        __ritPerMaand.zetTotaalKosten(ritPerMaandJSON['totaalKosten'])
        for reisDagJSON in ritPerMaandJSON['reisDagen']:
            __reisDagDatum = datetime.datetime.strptime(reisDagJSON, '%d-%m-%Y')
            __reisDag = reisDag(__reisDagDatum)
            __reisDag.zetTotaalAfstand(ritPerMaandJSON['reisDagen'][reisDagJSON]['totaalAfstand'])
            __reisDag.zetTotaalKosten(ritPerMaandJSON['reisDagen'][reisDagJSON]['totaalKosten'])
            __ritPerMaand.nieuweReisDagToevoegen(__reisDag)
            rittenJSON = ritPerMaandJSON['reisDagen'][reisDagJSON]['ritten']
            for ritJSON in rittenJSON:
                __rit = rit(rittenJSON[ritJSON]['startPostcode'], rittenJSON[ritJSON]['doelPostcode'], rittenJSON[ritJSON]['afstand'], rittenJSON[ritJSON]['omschrijving'])
                __reisDag.nieuweRitToevoegen(__rit)
        return __ritPerMaand

    def __maakJSON(self, ritPerMaand):
        ritPerMaandJSON = {}
        ritPerMaandJSON['maand'] = ritPerMaand.getMaand()
        ritPerMaandJSON['jaar'] = ritPerMaand.getJaar()
        ritPerMaandJSON['totaalAfstand'] = ritPerMaand.getTotaalAfstand()
        ritPerMaandJSON['totaalKosten'] = ritPerMaand.getTotaalKosten()
        ritPerMaandJSON['reisDagen'] = {}
        for reisDag in ritPerMaand.getAlleReisDagen():
            ritPerMaandJSON['reisDagen'][reisDag.getDatum()] = {}
            ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['totaalAfstand'] = reisDag.getTotaalAfstand()
            ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['totaalKosten'] = reisDag.getTotaalKosten()
            ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['ritten'] = {}
            for rit in reisDag.getAlleRitten():
                ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['ritten'][rit.getNummer()] = {}
                ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['ritten'][rit.getNummer()]['startPostcode'] = rit.getStartPostcode()
                ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['ritten'][rit.getNummer()]['doelPostcode'] = rit.getDoelPostcode()
                ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['ritten'][rit.getNummer()]['afstand'] = rit.getAfstand()
                ritPerMaandJSON['reisDagen'][reisDag.getDatum()]['ritten'][rit.getNummer()]['omschrijving'] = rit.getOmschrijving()
        return json.dumps(ritPerMaandJSON)

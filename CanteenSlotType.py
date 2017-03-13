from Constants import *


class CanteenSlotType(object):

    @staticmethod
    def getIds(name):
        if name is None:
            return []
        name = name.lower()
        ids = []
        if "strana" in name or "nationen" in name:
            if "mensa" in name:
                ids.append(ID_MENSA_STRANA)
            elif "cafeteria" in name:
                ids.append(ID_CAFETERIA_STRANA)
            else:
                ids.extend([ID_MENSA_STRANA, ID_CAFETERIA_STRANA])
        elif "reichen" in name:
            if "mensa" in name:
                ids.append(ID_MENSA_REICHENHAIN)
            elif "cafeteria" in name:
                ids.append(ID_CAFETERIA_REICHENHAIN)
            else:
                ids.extend([ID_MENSA_REICHENHAIN, ID_CAFETERIA_REICHENHAIN])
        return ids

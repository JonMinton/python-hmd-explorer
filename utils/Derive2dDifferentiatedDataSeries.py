

def derive2DDifferentiatedDataSeries(ySeriesDict):
    def getDiffsAsDict(dct):
        k = list(dct.keys())
        v = list(dct.values())
        vDiff = [b-a for a, b in zip(v, v[1:])]

        out = {k[i]: vDiff[i] for i in range(len(k) - 1)}
        return out

    out = dict()
    for k, v in ySeriesDict.items():
        out[k] = getDiffsAsDict(v)
    return out
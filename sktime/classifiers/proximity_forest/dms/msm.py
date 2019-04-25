from classifiers.proximity_forest.dms.distance_measure import DistanceMeasure
from classifiers.proximity_forest.dms.dtw import Dtw

from datasets import load_gunpoint
from distances import msm_distance


class Msm(Dtw):

    cost_key = 'cost'
    default_cost = 1

    def __init__(self, **params):
        self._cost = None
        super(Msm, self).__init__(**params)

    def find_distance(self, a, b, cut_off):
        return msm_distance(a, b, **self.get_params())

    def set_params(self, **params):
        super(Msm, self).set_params(**params)
        super(Msm, self)._set_param(self.cost_key, self.default_cost, params)

    def get_params(self):
        return {self.cost_key: self._cost, **super(Msm, self).get_params()}

if __name__ == "__main__":
    x_train, y_train = load_gunpoint(return_X_y=True)
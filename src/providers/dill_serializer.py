"""
    default way to serialize the feature extraction pipeline
"""

import dill
from src.providers.serializer_base import Serializer_Base

class Dill_Serializer(Serializer_Base):
    
    def __init__(self, config):
        self.config = config

    def encode(self, obj, **kwargs):
        dill.settings['recurse'] = True
        dumps = dill.dumps(obj)
        return dumps

    def decode(self, dumps, **kwargs):
        pipeline = dill.loads(dumps)
        return pipeline


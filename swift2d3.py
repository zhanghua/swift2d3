'''
Created on Jul 3, 2014

@author: Zhang Hua
'''

import sys
import pprint

from swift.common.ring import Ring
from swift.common.ring.utils import build_tier_tree

class Ring2D3(object):
    
    def __init__(self, ring_path):
        self.ring = Ring(ring_path)
        self.pp = pprint.PrettyPrinter()

    def tod3(self):
        pass

    def toconsole(self):
        pd = []
        for p in xrange(self.ring.partition_count):
            nodes = self.ring.get_part_nodes(p)
            nd = []
            for n in nodes:
                nd.append((p, n['id'], '%(device)s@%(ip)s:%(port)d/%(region)s' % n, n['weight']))
            pd.append(nd)
        self.pp.pprint(pd)
        
        self.pp.pprint(build_tier_tree(self.ring.devs))


def main(args=None):
    args = args or sys.argv
    if len(args)>1:
        r2d3 = Ring2D3(args[1])
        r2d3.toconsole()
    else:
        print 'please input the path of ring file'
        exit(0)

if __name__ == "__main__":
    sys.exit(main())


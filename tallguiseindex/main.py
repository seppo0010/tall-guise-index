import os
import sys

import providers

def main(recipe):
    provider = os.environ.get('TGI_PROVIDER', 'coto')
    klass = getattr(getattr(providers, provider), provider[0].upper() + provider[1:]);
    instance = klass()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('usage: {} <recipe>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])

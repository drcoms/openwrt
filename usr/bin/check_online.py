import sys
import os


def check_online():
    # avoiding timeout error
    try:
        # wget would exist if busybox is installed
        # test if http://www.baidu.com in http://baidu.com
        ret = os.system('wget http://baidu.com -O /tmp/drcom_chkofl')
        if ret != 0:
            # wget error happened
            return False

        with open('/tmp/drcom_chkofl', 'r') as f:
            txt = f.read()
            if 'http://www.baidu.com' not in txt:
                return False

    except:
        return False

    return True

if check_online():
    sys.exit(1)

sys.exit(0)

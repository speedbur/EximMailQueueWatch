import main
import unittest

import settings


class TestParser(unittest.TestCase):

    def test_check_mail_queue_size(self):
        main.check_mail_queue_size("20")

        exceeded_value = str(settings.EXIM_WARN_QUEUE_SIZE + 1)
        self.assertRaises(Exception, lambda: main.check_mail_queue_size(exceeded_value))

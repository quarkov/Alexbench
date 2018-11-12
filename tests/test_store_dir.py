from unittest import TestCase
from core.store_dir import*
from os import*


class TestStoreDir(TestCase):
    hs_list = [
                "dynatrace.com",
                "xyz.com",
                "google.com",
                "spacex.com",
                "techcrunch.com"
              ]
    current_dir = getcwd()

    def test_nesting_folders(self):
        sub_f_count = 10
        for hs in self.hs_list:
            for i in range(sub_f_count):
                store_dir(hs)
                chdir(self.current_dir)
                res_dir = path.join("./results", hs, str(datetime.now()).split()[0], str(i+1))
                self.assertTrue(path.exists(res_dir))
                print('nested folders created:', res_dir)
            for j in range(sub_f_count):
                res_dir = path.join("./results", hs, str(datetime.now()).split()[0], str(j + 1))
                removedirs(res_dir)
                print('nested folders deleted:', res_dir)

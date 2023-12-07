import unittest
import python_lab01_B_PIN_RIS_2106_Lutiy_Maksim

class TestInsertionSort(unittest.TestCase):
    
    def test_sort(self):
        ls = [5,10,4,1,11,23]
        ls2 = [1,4,5,10,11,23]
        python_lab01_B_PIN_RIS_2106_Lutiy_Maksim.insertion_sort(ls)
        self.assertEqual(ls,ls2,"Тест сортировки вставками не выполнен!")

if __name__ == '__main__':
    unittest.main()
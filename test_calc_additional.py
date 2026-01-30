import unittest
from calc_mul import calc

class TestCalcAdditional(unittest.TestCase):

        # ==============================
        # 正常系（同値クラス：有効）
        # ==============================

        def test_normal_case (self):
                self.assertEqual(21, calc(3,7))

        # 境界値（有効範囲）
        def test_boundary_min (self):
                self.assertEqual(1, calc(1,1))

        def test_boundary_max (self):
                self.assertEqual(998001, calc(999,999))


        # ==============================
        # 範囲外（Aのみ不正）
        # ==============================

        def test_a_out_of_range_lower (self):
                self.assertEqual(-1, calc(0,10))

        def test_a_out_of_range_upper (self):
                self.assertEqual(-1, calc(1000,10))

        def test_a_negative (self):
                self.assertEqual(-1, calc(-5,10))


        # ==============================
        # 範囲外（Bのみ不正）
        # ==============================

        def test_b_out_of_range_lower (self):
                self.assertEqual(-1, calc(10,0))

        def test_b_out_of_range_upper (self):
                self.assertEqual(-1, calc(10,1000))

        def test_b_negative (self):
                self.assertEqual(-1, calc(10,-3))


        # ==============================
        # 両方が範囲外
        # ==============================

        def test_both_out_of_range (self):
                self.assertEqual(-1, calc(0,1000))


        # ==============================
        # 型不正（Aのみ）
        # ==============================

        def test_a_float (self):
                self.assertEqual(-1, calc(0.5,10))

        def test_a_string (self):
                self.assertEqual(-1, calc("a",10))


        # ==============================
        # 型不正（Bのみ）
        # ==============================

        def test_b_float (self):
                self.assertEqual(-1, calc(10,0.5))

        def test_b_string (self):
                self.assertEqual(-1, calc(10,"b"))


        # ==============================
        # 両方が型不正


        def test_both_string (self):
                self.assertEqual(-1, calc("a","b"))

        def test_both_float (self):
                self.assertEqual(-1, calc(0.1,1.2))
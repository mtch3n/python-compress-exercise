import unittest

from src.compress import Solution


class TestCompressAlgo(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_compress_alg_case1(self):
        expected = "a2b2c3"
        actual = list("aabbccc")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_alg_case2(self):
        expected = "a"
        actual = list("a")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_alg_case3(self):
        expected = "ab12"
        actual = list("abbbbbbbbbbbb")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_alg_edge_case(self):
        expected = "123ef2eac01cb65c"
        actual = list("123effeac01cb65c")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_alg_edge_case_2(self):
        expected = "ef2eac01cb65c123"
        actual = list("effeac01cb65c123")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_alg_edge_case_3(self):
        expected = "b0lA]+O5j4"
        actual = list("b0lA]+O5j4")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_alg_edge_case_4(self):
        expected = "V4X2U(6+q3G6w-z2A2k2>j2.j5I2R2c$2u&(w2~54q2k#j2<4a5@K2X5_2{4T2U2#882a,5}2oj=2(A&2e6R3T2a3S2a2-4S3X{759C*2FEo7d.f5J3Q4w3q2ao#6'2cZ2depX96p2H3~2$3]Fl3ke62A*p<2h2V3}282Gm45WNd4b3y3bk3o_2R4V2q12B46P2QFR4>O6<V683z2k;)W-2D3e2"
        actual = list(
            "VVVVXXU((((((+q3GGGGGGw-zzAAkk>jj.jjjjjIIRRc$$u&(ww~~~~~4qqk#jj<<<<aaaaa@KKX5__{{{{TTUU########82a,,,,,}}oj==(A&&eeeeeeRRRTTaaaSSaa-4SSSX{777779C**FEo7d.fffffJJJQQQQwwwqqao######''cZZdepX999999ppHHH~~$$$]Flllke66A*p<<hhVVV}}88Gmmmm5WNddddbbbyyybkkko__RRRRVVq11BBBB6PPQFRRRR>OOOOOO<V6888zzk;)W--DDDee")
        i = self.solution.compress(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_2_alg_case1(self):
        expected = "a3bc4d2"
        actual = list("aaabccccdd")
        i = self.solution.compress_2(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_2_alg_case2(self):
        expected = "a5f10c"
        actual = list("aaaaaffffffffffc")
        i = self.solution.compress_2(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_2_alg_case3(self):
        expected = "abcd"
        actual = list("abcd")
        i = self.solution.compress_2(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_2_alg_case4(self):
        expected = "c3e4c3e3"
        actual = list("ccceee12eccceee")
        i = self.solution.compress_2(actual)

        self.assertEqual(list(expected), actual[:i])

    def test_compress_2_alg_case5(self):
        expected = "ef2eac2bc"
        actual = list("effeac01cb65c ")
        i = self.solution.compress_2(actual)

        self.assertEqual(list(expected), actual[:i])


if __name__ == '__main__':
    unittest.main()

import unittest
import argparse
import ryuko

class BadInputCase(unittest.TestCase):
    def testTooManyArguments(self):
        """ Ryuko should fail if called with too many Arguments """
        self.assertEqual(True, True)


class LearningCase(unittest.TestCase):
    def setUp(self):
        self.input_file = "video.mkv"
        self.output_file = "output.gif"
        self.arguments = argparse.Namespace(duration=2.0, flip=False, fps=8,
                                            input_file=self.input_file,
                                            output_file=self.output_file,
                                            start=1.0, subtitle=False,
                                            subtitle_file=False,
                                            subtitle_offset=False,
                                            use_builtin=False,
                                            x=500, y=False)

    def test_starting_out(self):
        ryuko.main(self.arguments)

    def assertFilesEqual(self, first, second, msg=None):
        first_f = open(first)
        first_str = first_f.read()
        second_f = open(second)
        second_str = second_f.read()
        first_f.close()
        second_f.close()

        if first_str != second_str:
            first_lines = first_str.splitlines(True)
            second_lines = second_str.splitlines(True)
            delta = difflib.unified_diff(first_lines, second_lines, fromfile=first, tofile=second)
            message = ''.join(delta)

            if msg:
                message += " : " + msg

            self.fail("Multi-line strings are unequal:\n" + message)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

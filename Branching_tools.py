import sys

class BranchingNodeClass:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "A_Line": ("INT", {"default": 0, "min": 0, "max": sys.maxsize, "step": 1}),
                "B_Line": ("INT", {"default": 0, "min": 0, "max": sys.maxsize, "step": 1}),
                "counter": ("INT", {"default": 0, "min": 0, "max": sys.maxsize, "step": 1}),
            },
        }    

    RETURN_TYPES = ("INT", "INT", )
    RETURN_NAMES = ("index_A", "index_B",)
    OUTPUT_NODE = True
    CATEGORY = "Branching_Line"
    FUNCTION = "compare"

#A_Line, B_Lineにはテキストの行数を代入

    def compare(self, A_Line, B_Line, counter):
        result_A=0
        result_B=0
        if B_Line > A_Line:
            result_A = (counter - counter % B_Line) % A_Line
            result_B = counter % B_Line
        else:
            result_A = (counter // B_Line) % A_Line
            result_B = counter % B_Line

        return (result_A, result_B, )
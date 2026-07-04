import ctypes
import os
import sys

class LshBridge:
    def __init__(self):
        if not os.path.exists("./liblsh.so") and not os.path.exists("./liblsh.dll"):
            if sys.platform.startswith("win"):
                os.system("gcc -shared -o liblsh.dll lsh_router.c")
                lib_path = "./liblsh.dll"
            else:
                os.system("gcc -shared -fPIC -o liblsh.so lsh_router.c")
                lib_path = "./liblsh.so"
        else:
            lib_path = "./liblsh.dll" if sys.platform.startswith("win") else "./liblru.so"

        self.lib = ctypes.CDLL(lib_path)
        self.lib.init_lsh_cluster.restype = ctypes.c_void_p
        self.lib.map_node_signature.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
        self.lib.calculate_lsh_bucket.argtypes = [ctypes.POINTER(ctypes.c_float)]
        self.lib.calculate_lsh_bucket.restype = ctypes.c_int
        
        self.lsh_ptr = self.lib.init_lsh_cluster()

    def process_node_data(self, dataset_id: int, vector: list):
        c_array = (ctypes.c_float * len(vector))(*vector)
        self.lib.map_node_signature(self.lsh_ptr, dataset_id, c_array)

    def route_vector_query(self, query_vector: list) -> int:
        c_array = (ctypes.c_float * len(query_vector))(*query_vector)
        return self.lib.calculate_lsh_bucket(c_array)

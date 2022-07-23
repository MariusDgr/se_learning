def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != len(original):
        return []
    
    mtrx = []
    for i in range(m):
        mtrx.append(original[i*n:(i+1)*n])
                    
    return mtrx

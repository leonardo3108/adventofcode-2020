init = []
for linha in open('input-17.txt'):
    init.append(linha.strip())

#init = ['.#.', '..#', '###']

cycle = 0
init_size = len(init[0])

#print(cycle, hipercubes)

def get_size():
    return cycle * 2 + init_size
    
def new_3D_slice(size):
    return [['.' * size] * size] * size
        
def new_slice(size):
    return ['.' * size] * size
        
def new_line(size):
    return '.' * size
        
def expand_slice(slice, size):
    slice.insert(0, new_line(size))
    slice.append(new_line(size))
    for i, line in enumerate(slice[1:-1]):
        slice[i+1] = '.' + line + '.'
    
def expand_3D_slice(slice3D, size):
    slice3D.insert(0, new_slice(size))
    slice3D.append(new_slice(size))
    for slice in slice3D[1:-1]:
        expand_slice(slice, size)

def expand(hipercubes, size):
    hipercubes.insert(0, new_3D_slice(size))
    hipercubes.append(new_3D_slice(size))
    for slice3D in hipercubes[1:-1]:
        expand_3D_slice(slice3D, size)

def get_cube(hipercubes, i, j, k, l):
    if i < 0 or j < 0 or k < 0 or l < 0 or i >= len(hipercubes) or j >= len(hipercubes[i]) or k >= len(hipercubes[i][j]) or l >= len(hipercubes[i][j][k]):
        return '.'
    return hipercubes[i][j][k][l]
    
def change_hipercube(hipercube, i, j, k, l, hipercubes):
    result = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            for z in range(k-1, k+2):
                if l < 0:
                    if x != i or y != j or z != k:
                        result += get_cube(hipercubes, x, y, z, 0) == '#'
                else:
                    for w in range(l-1, l+2):
                        if x != i or y != j or z != k or w != l:
                            result += get_cube(hipercubes, x, y, z, w) == '#'
                    
    #If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    #If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    if result == 3 or hipercube == '#' and result == 2:
        return '#'
    else:
        return '.'
    return str(result)

def change(cubes):
    ncubes = []
    for i, slice in enumerate(cubes):
        nslice = []
        for j, line in enumerate(slice):
            nline = ''
            for k, cube in enumerate(line):
                nline += change_hipercube(cube, i, j, k, -1, cubes)
            nslice.append(nline)
        ncubes.append(nslice)
    return ncubes
    
def change_4D(hipercubes):
    ncubes = []
    for i, slice3D in enumerate(hipercubes):
        nslice3D = []
        for j, slice in enumerate(slice3D):
            nslice = []
            for k, line in enumerate(slice):
                nline = ''
                for l, hipercube in enumerate(line):
                    nline += change_hipercube(hipercube, i, j, k, l, hipercubes)
                nslice.append(nline)
            nslice3D.append(nslice)
        ncubes.append(nslice3D)
    return ncubes
    
def evolve(cycle, cubes):
    expand_3D_slice(cubes, cycle * 2 + init_size + 2)
    ncubes = change(cubes)
    return cycle + 1, ncubes
    
def evolve_4D(cycle, hipercubes):
    expand(hipercubes, cycle * 2 + init_size + 2)
    nhipercubes = change_4D(hipercubes)
    return cycle + 1, nhipercubes

def count_actives(cubes):
    result = 0
    for slice in cubes:
        for line in slice:
            for cube in line:
                result += cube == '#'
    return result

def count_actives_4D(hipercubes):
    result = 0
    for slice3D in hipercubes:
        for slice in slice3D:
            for line in slice:
                for hipercube in line:
                    result += hipercube == '#'
    return result

cubes = [init]

for i in range(0, 6):
    cycle, cubes = evolve(cycle, cubes)
print(count_actives(cubes))

hipercubes = [[init]]
print()

for i in range(0, 6):
    cycle, hipercubes = evolve_4D(cycle, hipercubes)
    print(count_actives_4D(hipercubes))
    

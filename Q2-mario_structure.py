def build_right_triangle(struct_range, struct_des):
    space = struct_range
    lines = []
    for right_tri in range(1, struct_range + 1):
        space -= 1
        lines.append((space * " ") + (right_tri * struct_des))
    return lines

def build_left_triangle(struct_range, struct_des):
    lines = []
    for left_tri in range(1, struct_range + 1):
        lines.append(left_tri * struct_des)
    return lines

def build_square(struct_range, struct_des):
    lines = []
    for square in range(1, struct_range + 1):
        lines.append((struct_range + 1) * struct_des)
    return lines

while True:
    struc_no = int(input("Enter number of structures (1 to 3): "))
    if struc_no < 1 or struc_no > 3:
        print("Please enter a valid number between 1 and 3.")
    else:
        break

all_structures = []

for i in range(1, struc_no + 1):
    struct_type = input(f"\nStructure {i} : \nType (triangle or square): ")
    
    while True:
        struct_range = int(input("Height (1 to 10): "))
        if struct_range < 1 or struct_range > 10:
            print("Invalid height. Please enter a value between 1 and 10.")
        else:
            break

    struct_des = input("Character (e.g. *, #): ")
    if struct_type.lower() == "triangle":
        while True:
            align = input("Alignment (Right or Left): ")
            if align.lower() == "right":
                shape= build_right_triangle(struct_range, struct_des)
                break
            elif align.lower() == "left":
                shape = build_left_triangle(struct_range, struct_des)
                break
    elif struct_type.lower() == "square":
        shape = build_square(struct_range, struct_des)

    all_structures.append(shape)

max_height = max(len(shape) for shape in all_structures)
for row_index in range(max_height):  
    for shape in all_structures:    
        if row_index < len(shape):
            print(shape[row_index], end="  ")
        else:
            print(" " * len(shape[0]), end=" ")
    print()
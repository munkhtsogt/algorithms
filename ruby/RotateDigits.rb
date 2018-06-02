def rotate_digits(n)
    count = 0
    map = {
        0 => 0,
        1 => 1,
        2 => 5,
        5 => 2,
        6 => 9,
        8 => 8,
        9 => 6,
    }

    for i in 1 ... n + 1
        j, r, p, valid = i, 0, 0, true
        while j != 0
            if map.has_key? j % 10
                r += map[j % 10] * 10 ** p
            else
                valid = false
                break
            end
            p += 1
            j /= 10
        end
        if valid && r != i
            count += 1
        end
    end
    count
end

print rotate_digits(10)
'''
CIS 122 Fall 2018 Lab 7
Author: Jacob Rammer
Partner: None
Description: Display the stats of the file
'''


def count():
    """Count the lines in txt file
    Count the number of lines in the text file
    :return: Line count
    """
    fin = open("words_alpha.txt")
    line_count = 0
    for line in fin:
        line_count += 1
    fin.close()
    return line_count


def longest_word():
    """Find longest word
    Find the longest word in the text file
    :return: The longest word as a string
    """
    doc_longest_word = ""
    fin = open("words_alpha.txt")
    for line in fin:
        line = line.strip()
        if len(line) > len(doc_longest_word):
            doc_longest_word = line
    fin.close()
    return doc_longest_word


def shortest_word():
    """Find the shortest word
    Find a word that is the shortest and break instantly
    :return:  Shortest word as a string
    """
    doc_shortest_word = ' '
    fin = open("words_alpha.txt")
    for line in fin:
        line = line.strip()
        if len(line) <= len(doc_shortest_word):
            doc_shortest_word = line
            break
    fin.close()
    return doc_shortest_word


def is_palindrome():
    """Determine if a word is a palindrome
    Search whole document for palindromes (words that are the same reversed)
    :return: Number of palindromes
    """
    palindrome = 0
    fin = open("words_alpha.txt")
    for line in fin:
        line = line.strip()
        p_word = line[::-1]
        if line == p_word:
            palindrome += 1
    fin.close()
    return palindrome


def calculate_start_char():
    """Prints a lot of stuff
    Checks to see how many words start with each letter
    and prints result
    :return: Void
    """
    line_count = count()
    print("First letter counts")
    fin = open("words_alpha.txt")
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t \
        = u = v = w = x = y = z = other = 0
    for line in fin:
        line = line.strip()
        if line[0:1] == "a":
            a += 1
        elif line[0:1] == "b":
            b += 1
        elif line[0:1] == "c":
            c += 1
        elif line[0:1] == "d":
            d += 1
        elif line[0:1] == "e":
            e += 1
        elif line[0:1] == "f":
            f += 1
        elif line[0:1] == "g":
            g += 1
        elif line[0:1] == "h":
            h += 1
        elif line[0:1] == "i":
            i += 1
        elif line[0:1] == "j":
            j += 1
        elif line[0:1] == "k":
            k += 1
        elif line[0:1] == "l":
            l += 1
        elif line[0:1] == "m":
            m += 1
        elif line[0:1] == "n":
            n += 1
        elif line[0:1] == "o":
            o += 1
        elif line[0:1] == "p":
            p += 1
        elif line[0:1] == "q":
            q += 1
        elif line[0:1] == "r":
            r += 1
        elif line[0:1] == "s":
            s += 1
        elif line[0:1] == "t":
            t += 1
        elif line[0:1] == "u":
            u += 1
        elif line[0:1] == "v":
            v += 1
        elif line[0:1] == "w":
            w += 1
        elif line[0:1] == "x":
            x += 1
        elif line[0:1] == "y":
            y += 1
        elif line[0:1] == "z":
            z += 1
        else:
            other += 1

    print("A:", a, " (", round(a / line_count * 100, 2), "%)", sep="")
    print("B:", b, " (", round(b / line_count * 100, 2), "%)", sep="")
    print("C:", c, " (", round(c / line_count * 100, 2), "%)", sep="")
    print("D:", d, " (", round(d / line_count * 100, 2), "%)", sep="")
    print("E:", e, " (", round(e / line_count * 100, 2), "%)", sep="")
    print("F:", f, " (", round(f / line_count * 100, 2), "%)", sep="")
    print("G:", g, " (", round(g / line_count * 100, 2), "%)", sep="")
    print("H:", h, " (", round(h / line_count * 100, 2), "%)", sep="")
    print("I:", i, " (", round(i / line_count * 100, 2), "%)", sep="")
    print("J:", j, " (", round(j / line_count * 100, 2), "%)", sep="")
    print("K:", k, " (", round(k / line_count * 100, 2), "%)", sep="")
    print("L:", l, " (", round(l / line_count * 100, 2), "%)", sep="")
    print("M:", m, " (", round(m / line_count * 100, 2), "%)", sep="")
    print("N:", n, " (", round(n / line_count * 100, 2), "%)", sep="")
    print("O:", o, " (", round(o / line_count * 100, 2), "%)", sep="")
    print("P:", p, " (", round(p / line_count * 100, 2), "%)", sep="")
    print("Q:", q, " (", round(q / line_count * 100, 2), "%)", sep="")
    print("R:", r, " (", round(r / line_count * 100, 2), "%)", sep="")
    print("S:", s, " (", round(s / line_count * 100, 2), "%)", sep="")
    print("T:", t, " (", round(t / line_count * 100, 2), "%)", sep="")
    print("U:", u, " (", round(u / line_count * 100, 2), "%)", sep="")
    print("V:", v, " (", round(v / line_count * 100, 2), "%)", sep="")
    print("W:", w, " (", round(w / line_count * 100, 2), "%)", sep="")
    print("X:", x, " (", round(x / line_count * 100, 2), "%)", sep="")
    print("Y:", y, " (", round(y / line_count * 100, 2), "%)", sep="")
    print("Z:", z, " (", round(z / line_count * 100, 2), "%)", sep="")
    print("Other: ", other, " (", round(other / line_count * 100, 2), ")", sep="")
    fin.close()


def print_results():
    """Print results
    Call all the functions in program and calculate the results
    :return: Void (as of now)
    """
    line_count = count()
    doc_longest_word = longest_word()
    doc_shortest_word = shortest_word()
    palindrome = is_palindrome()

    print("Longest word is: ", doc_longest_word, " (", len(doc_longest_word), ")", sep="")
    print("Shortest word is: ", doc_shortest_word, " (", len(doc_shortest_word), ")", sep="")
    print("Palindromes: ", palindrome, "(", round(palindrome / line_count * 100, 2), "%)", sep="")
    calculate_start_char()


print_results()

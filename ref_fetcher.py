import sys

def main(argv):
    f_in = open(TEXFILE)

    REFERENCES = []
    current_word = ''
    found_beginning = False
    in_cite = False

    for line in f_in:
        ## sometimes there might be a cite command in the preamble
        ## as option
        if line.startswith("\\begin{document}"):
            found_beginning = True
        if not found_beginning:
            continue
        
        for ch in line:
            if not in_cite:
                if ch != ' ' and ch != '\n' and ch != '\t' and ch != '\\':
                    current_word += ch
                else:
                    current_word = ''
                if ch == '{':
                    if current_word.startswith('cite'):
                        in_cite = True
                        current_word = ''
            else:
                if ch != '}':
                    current_word += ch
                else:
                    in_cite = False
                    current_word = [x.strip() for x in current_word.split(',')]
                    REFERENCES.append(current_word)
                    current_word = ''
    REFERENCES = [item for sublist in REFERENCES for item in sublist]
    print REFERENCES

if __name__ == '__main__':
    ## either with cmdline or with var
    try:
        TEXFILE = str(sys.argv[1:][0])
    except IndexError:
        TEXFILE = '/Users/dimitriosalikaniotis/Documents/docs/Approximating semantic structures using high-dimensional lexical spaces/TeX/draft.tex'
    main(TEXFILE)
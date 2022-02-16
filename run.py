from pydub import AudioSegment
from pydub.playback import play
import re 
import random

def play_files(filenames):
    print('playing ', len(filenames), 'files')

    print(filenames)
    combined = sum(map(AudioSegment.from_wav, map(lambda f: 'assets/' + f,filenames)))
    play(combined)


wav_list1= """2   96   22  141   41  105  122   11   30   70  121   26    9  112   49  109   14
  3   32    6  128   63  146   46  134   81  117   39  126   56  174   18  116   83
  4   69   95  158   13  153   55  110   24   66  139   15  132   73   58  145   79
  5   40   17  113   85  161    2  159  100   90  176    7   34   67  160   52  170
  6  148   74  163   45   80   97   36  107   25  143   64  125   76  136    1   93
  7  104  157   27  167  154   68  118   91  138   71  150   29  101  162   23  151
  8  152   60  171   53   99  133   21  127   16  155   57  175   43  168   89  172
  9  119   84  114   50  140   86  169   94  120   88   48  166   51  115   72  111
 10   98  142   42  156   75  129   62  123   65   77   19   82  137   38  149    8
 11    3   87  165   61  135   47  147   33  102    4   31  164  144   59  173   78
 12   54  130   10  103   28   37  106    5   35   20  108   92   12  124   44  131"""

wav_list2="""1  72   6  59  25  81  41  89  13  36   5  46  79  30  95  19  66
 2  56  82  42  74  14   7  26  71  76  20  64  84   8  35  47  88
 3  75  39  54   1  65  43  15  80   9  34  93  48  69  58  90  21
 4  40  73  16  68  29  55   2  61  22  67  49  77  57  87  33  10
 5  83   3  28  53  37  17  44  70  63  85  32  96  12  23  50  91
 6  18  45  62  38   4  27  52  94  11  92  24  86  51  60  78  31"""

new_lines = []
def listing_the_wav(wav_list):
    lines= wav_list.split('\n')
    lines_split_into_arrays= list(map(lambda line: re.split(' +', line.strip()), lines))
    columns=[]
    for x in range(1,17):
        column_group=[]
        for a_line_as_array in lines_split_into_arrays:
            column_group.append(a_line_as_array [x])
        #column_group2 = [a_line_as_array [x] for a_line_as_array in lines_split_into_arrays]
        print ('column_group', x, column_group)
        columns.append(column_group)
    columns = [[a_line_as_array[x] for a_line_as_array in lines_split_into_arrays] for x in range(1,17)]
    return columns



col1 = listing_the_wav(wav_list1)
col2 = listing_the_wav(wav_list2)


columns_count= len(col1)
print (columns_count)

the_first_piece = list(map(random.choice, col1 ))
print('the_first_piece', len(the_first_piece), the_first_piece)

the_second_piece=list(map(random.choice, col2))
print('the_second_piece', len(the_second_piece), the_second_piece)

#play_files(['M64.wav','M65.wav'])

the_1_piece=list(map(lambda x : "M{}.wav".format(x),the_first_piece))
print (the_1_piece)
the_2_piece= list(map(lambda x : "T{}.wav".format(x),the_second_piece))
print (the_2_piece)

the_final_piece=the_1_piece + the_2_piece 
print ('the_final_piece', the_final_piece)
play_files(the_final_piece)
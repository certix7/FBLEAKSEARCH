# Copyright (C) 2021 EHAuthority
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# [NOTES] -----------------------------------------------------------
# 1) Tested on Linux (debian), Windows 10
# 2) I'm not responsible about how you will use it, use it at your own.
# 3) Your free to change the tool depending on your file format if it didn't work
# --------------------------------------------------------------------

import pandas as pd
import optparse


def dataSearch(txt, id, phone, csv):
    try:
        file = open(txt, 'r', encoding='utf8')
    except (FileNotFoundError, IOError):
        print("Wrong file or file path")
        quit()
    nonempty_lines = [line.strip("\n").split(":") for line in file]

    df = pd.DataFrame(nonempty_lines,
                      columns=['phone', 'id', 'first_name', 'last_name', 'gender', 'hometown', 'country',
                               'relationship', 'job', 'date', 'email', 'birthday'])
    finalresult = pd.DataFrame(columns=['phone', 'id', 'first_name', 'last_name', 'gender', 'hometown', 'country',
                                        'relationship', 'job', 'date', 'email', 'birthday'])
    if phone:
        ph = df[df['phone'].str.contains(str(phone))]
        if not ph.equals(finalresult):
            finalresult = finalresult.append(ph)

    if id:
        fid = df[df['id'].str.contains(id)]
        if not fid.equals(finalresult):
            finalresult = finalresult.append(fid)
    if csv:
        try:
            df.to_csv(csv, index=False, )
        except:
            print("write the directory with file name like : /home/out.csv")
    print(finalresult)


def printImportantfunc():
    print("#" * 60)
    print("this tool made by : D3ADR00T\n website : https://ehauthority.blogspot.com/")
    print("#" * 60)

def Main():
    printImportantfunc()
    parser = optparse.OptionParser('usage --txt ' + '--id <facebookId> --phone <phone> --csv <output csv>')

    parser.add_option('--txt', dest='txt', type='string', help='specify text file ')
    parser.add_option('--id', dest='id', type='string', help='specify facebook id ')
    parser.add_option('--phone', dest='phone', type='string', help='specify phone number ')
    parser.add_option('--csv', dest='csv', type='string', help='specify output csv file ')

    (options, args) = parser.parse_args()
    if (options.txt is None) | (options.id is None) & (options.phone is None) & (options.csv is None):
        print(parser.usage)
    else:
        id = options.id
        phone = options.phone
        txt = options.txt
        csv = options.csv

        dataSearch(txt, id, phone, csv)


if __name__ == '__main__':
    Main()

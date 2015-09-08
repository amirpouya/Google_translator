__author__ = 'AmirPouya'
import goslate
import sys,argparse
import io
parser=argparse.ArgumentParser('python LDC2XML.py')
parser.add_argument('--input','-i',required=True)
parser.add_argument('--output','-o',required=True)
parser.add_argument('--lang','-l',required=True)
args=parser.parse_args()

source_file=args.input
target_file=args.output

source_file=io.open(source_file,'r',encoding='utf-8')
source_lines=source_file.readlines()

target_file=io.open(target_file,'w',encoding='utf-8')

gs = goslate.Goslate()
for i,line in enumerate(source_lines):
    try:
        target_file.write(gs.translate(line, args.lang)+"\n")
        print i+1,'/', len(source_lines)
    except:
        C=None
        while C==None:
            try:
                C=(gs.translate(line, args.lang)+"\n")
                target_file.write(C+"\n")
                print 'Retry:', i+1,'/', len(source_lines)
            except:
                print 'Fialed',i+1
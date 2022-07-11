# For HLT =r22 Tau0 Comparison
dir=("emu_pt" "emu_RNN" "emu_dR" "emu_pt_RNN" "emu_pt_RNN_dR")
for i in 0 1 2 3 4
do
python3.9 emulation.py $i
#mv *.png ${dir[$i]}
done

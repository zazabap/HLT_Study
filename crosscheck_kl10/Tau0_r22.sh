# For HLT =r22 Tau0 Comparison
dir=("pt_Pass" "eta_Pass" "pt_PassFail" "eta_PassFail")
for i in 1 2 3 4
do
python3.9 Tau0_r22.py $i
mv r22_Pass_leading.png leading.png 
mv r22_Pass_Subleading.png Subleading.png
mv r22_Pass_Delta_R.png Delta_R.png 
mv r22_Pass_RNN_Score.png RNN_Score.png
mv r22_Pass_Prong.png Prong.png
mv *.png ${dir[$i-1]}
done

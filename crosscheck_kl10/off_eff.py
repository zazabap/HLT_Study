from sympy import true
from HLT_Study import *
from L1_HLT_cut import *

def off_tree_loop_cut_pt(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 10:
            inFile = ROOT.TFile.Open( input_root ,"READ")

    print("Start Looping ", taus[t])
    tree = inFile.Get("analysis")
    entries = range(tree.GetEntries())
    hltoff = []
####Off_Matched_Tau##################################################################################
    hist_offhltrnn = ROOT.TH1D("offhlt_rnn","",50,0,1)
    hist_offhltprong = ROOT.TH1D("offhlt_prong","",10,0,1)
    hist_offhltpt_r = ROOT.TH1D("offhltpt_r","",50,0,50)
    hist_offhltpt_lead_r = ROOT.TH1D("offhltpt_lead_r","",50,0,50)
    hist_offhltpt_sublead_r = ROOT.TH1D("offhltpt_sublead_r","",50,-1,4)

    hist_L1_offhltrnn = ROOT.TH1D("L1_offhlt_rnn","",50,0,1)
    hist_L1_offhltprong = ROOT.TH1D("L1_offhlt_prong","",10,0,1)
    hist_L1_offhltpt_r = ROOT.TH1D("L1_offhltpt_r","",50,0,50)
    hist_L1_offhltpt_lead_r = ROOT.TH1D("L1_offhltpt_lead_r","",50,0,50)
    hist_L1_offhltpt_sublead_r = ROOT.TH1D("L1_offhltpt_sublead_r","",50,-1,4)

    hist_HLT_offhltrnn = ROOT.TH1D("HLT_offhlt_rnn","",50,0,1)
    hist_HLT_offhltprong = ROOT.TH1D("HLT_offhlt_prong","",10,0,1)
    hist_HLT_offhltpt_r = ROOT.TH1D("HLT_offhltpt_r","",50,0,50)
    hist_HLT_offhltpt_lead_r = ROOT.TH1D("HLT_offhltpt_lead_r","",50,0,50)
    hist_HLT_offhltpt_sublead_r = ROOT.TH1D("HLT_offhltpt_sublead_r","",50,-1,4)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_J25")
        L1 = "L1_J25"
        # Bit confused about this point of trigger use 
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "r22_PassFail":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "Tau0_Pass":
            HLT_1 = getattr(tree, "HLT_J25_Tau0")
            HLT = "HLT_J20_Tau0"
        elif taus[t] == "Tau0_PassFail":
            HLT_1 = getattr(tree, "HLT_J25_Tau0")
            HLT = "HLT_J20_Tau0"

        for i in range(len(tree.Offline_Matched_Taus)):
            hist_offhltpt_r.Fill(tree.Offline_Matched_Taus[i].Pt(),1)
            if(i==0):
                hist_offhltpt_lead_r.Fill(tree.Offline_Matched_Taus[0].Pt(),1)
            if(i==1):
                hist_offhltpt_sublead_r.Fill(tree.Offline_Matched_Taus[1].Pt(),1)
        for j in range(len(tree.Off_Matched_TauRNN)):
            hist_offhltrnn.Fill(tree.Off_Matched_TauRNN[j],1)
        for k in range(len(tree.Off_Matched_TauProng)):
            hist_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

        # Should HLT be applied only after the L1 hardware trigger is passed? 
        if L1_1 :
            for i in range(len(tree.Offline_Matched_Taus)):
                hist_L1_offhltpt_r.Fill(tree.Offline_Matched_Taus[i].Pt(),1)
                if(i==0):
                    hist_L1_offhltpt_lead_r.Fill(tree.Offline_Matched_Taus[0].Pt(),1)
                if(i==1):
                    hist_L1_offhltpt_sublead_r.Fill(tree.Offline_Matched_Taus[1].Pt(),1)
            for j in range(len(tree.Off_Matched_TauRNN)):
                hist_L1_offhltrnn.Fill(tree.Off_Matched_TauRNN[j],1)
            for k in range(len(tree.Off_Matched_TauProng)):
                hist_L1_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)
            if HLT_1 :
                for i in range(len(tree.Offline_Matched_Taus)):
                    hist_HLT_offhltpt_r.Fill(tree.Offline_Matched_Taus[i].Pt(),1)
                    if(i==0):
                        hist_HLT_offhltpt_lead_r.Fill(tree.Offline_Matched_Taus[0].Pt(),1)
                    if(i==1):
                        hist_HLT_offhltpt_sublead_r.Fill(tree.Offline_Matched_Taus[1].Pt(),1)
                for j in range(len(tree.Off_Matched_TauRNN)):
                    hist_HLT_offhltrnn.Fill(tree.Off_Matched_TauRNN[j],1)
                for k in range(len(tree.Off_Matched_TauProng)):
                    hist_HLT_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

    hltoff.append(hist_offhltrnn)
    hltoff.append(hist_offhltprong)
    hltoff.append(hist_offhltpt_r)
    hltoff.append(hist_offhltpt_lead_r)
    hltoff.append(hist_offhltpt_sublead_r)

    hltoff.append(hist_L1_offhltrnn)
    hltoff.append(hist_L1_offhltprong)
    hltoff.append(hist_L1_offhltpt_r)
    hltoff.append(hist_L1_offhltpt_lead_r)
    hltoff.append(hist_L1_offhltpt_sublead_r)

    hltoff.append(hist_HLT_offhltrnn)
    hltoff.append(hist_HLT_offhltprong)
    hltoff.append(hist_HLT_offhltpt_r)
    hltoff.append(hist_HLT_offhltpt_lead_r)
    hltoff.append(hist_HLT_offhltpt_sublead_r)

def offline_efficiency(input_root, t):
    print("Offline Efficiency calculation based on HLT")

def main():
    tree_loop_cut_pt( "r22_Pass.root", 0)
    tree_loop_cut_eta( "r22_Pass.root", 0)

    tree_loop_cut_pt("r22_PassFail.root", 1)
    tree_loop_cut_eta("r22_PassFail.root", 1)

    tree_loop_cut_pt("Tau0_Pass.root", 2)
    tree_loop_cut_eta("Tau0_Pass.root", 2)

    tree_loop_cut_pt("Tau0_PassFail.root", 3)
    tree_loop_cut_eta("Tau0_PassFail.root", 3)


if __name__ == "__main__" :
    print("Hello, Start Ploting for HLT")
    main()
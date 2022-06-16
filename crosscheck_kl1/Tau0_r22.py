from sympy import true
import sys
from HLT_Study import *
from L1_HLT_cut import *

list_order=[
        "Prong", #5
        "RNN_Score", #12
        "Delta_R", #13
        "leading", #14
        "Subleading", #15
]

r_pt = [40,0,200]
def Tau0_r22_pt( Tau0_root, r22_root):
    for k in range(len(kL)):
        if kL[k] == 1:
            inTau0 = ROOT.TFile.Open( Tau0_root ,"READ")
            inr22 = ROOT.TFile.Open( r22_root ,"READ")
    
    tree = inr22.Get("analysis")
    entries = range(tree.GetEntries())

###################################################################################
#TrigMatched_Taus_HLTptfl##########################################################

    hist_HLT_onhltptpt_lead_r = ROOT.TH1D("HLT_onhltptpt_lead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_HLT_onhltptpt_sublead_r = ROOT.TH1D("HLT_onhltptpt_sublead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_HLT_onhltptrnn = ROOT.TH1D("HLT_onhltpt_rnn","",50,0,1)
    hist_HLT_onhltptprong = ROOT.TH1D("HLT_onhltpt_prong","",10,0,10)
    hist_HLT_onhltptdeltaR = ROOT.TH1D("HLT_onhltptdeltaR", "",50, -1, 4)

    # Manual Cut add later if necessary
    hist_m_onhltptpt_lead_r = ROOT.TH1D("m_onhltptpt_lead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_m_onhltptpt_sublead_r = ROOT.TH1D("m_onhltptpt_sublead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_m_onhltptrnn = ROOT.TH1D("m_onhltpt_rnn","",50,0,1)
    hist_m_onhltptprong = ROOT.TH1D("m_onhltpt_prong","",10,0,10)
    hist_m_onhltptdeltaR = ROOT.TH1D("m_onhltptdeltaR", "",50, -1, 4)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_J25")
        HLT_1 = getattr(tree, "HLT_J25_r22")
        if L1_1:
            if HLT_1:
                for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                    if(i==0):
                        hist_HLT_onhltptpt_lead_r.Fill(
                                tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if(i==1):
                        hist_HLT_onhltptpt_sublead_r.Fill(
                            tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                        vec0= tree.TrigMatched_Taus_HLTptfl[0].Vect()
                        vec1= tree.TrigMatched_Taus_HLTptfl[1].Vect()
                        hist_HLT_onhltptdeltaR.Fill(vec1.DeltaR(vec0))  
                for j in range(len(tree.TrigMatched_rnn_HLTptfl)):
                    hist_HLT_onhltptrnn.Fill(tree.TrigMatched_rnn_HLTptfl[j],1)
                for k in range(len(tree.TrigMatched_prong_HLTptfl)):
                    hist_HLT_onhltptprong.Fill(tree.TrigMatched_prong_HLTptfl[k], 1)
                    

    tree = inTau0.Get("analysis")
    entries = range(tree.GetEntries())

    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_J25")
        HLT_1 = getattr(tree, "HLT_J25_Tau0") 
        if L1_1:
            if HLT_1:
                if len(tree.TrigMatched_Taus_HLTptfl)<2 : continue
                for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                    if(i==0 and tree.TrigMatched_Taus_HLTptfl[0].Pt()>35
                        and tree.TrigMatched_Taus_HLTptfl[1].Pt()>25):
                        hist_m_onhltptpt_lead_r.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if(i==1 and tree.TrigMatched_Taus_HLTptfl[0].Pt()>35
                            and tree.TrigMatched_Taus_HLTptfl[1].Pt()>25):
                        hist_m_onhltptpt_sublead_r.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                        vec0= tree.TrigMatched_Taus_HLTptfl[0].Vect()
                        vec1= tree.TrigMatched_Taus_HLTptfl[1].Vect()
                        hist_m_onhltptdeltaR.Fill(vec1.DeltaR(vec0))  
                if(tree.TrigMatched_Taus_HLTptfl[0].Pt()>35
                    and tree.TrigMatched_Taus_HLTptfl[1].Pt()>25):
                    for j in range(len(tree.TrigMatched_rnn_HLTptfl)):
                        hist_m_onhltptrnn.Fill(tree.TrigMatched_rnn_HLTptfl[j],1)
                    for k in range(len(tree.TrigMatched_prong_HLTptfl)):
                        hist_m_onhltptprong.Fill(tree.TrigMatched_prong_HLTptfl[k], 1)
######################################################################################

    hlt_ratio = []

    hlt_ratio.append(hist_HLT_onhltptprong)
    hlt_ratio.append(hist_HLT_onhltptrnn)
    hlt_ratio.append(hist_HLT_onhltptdeltaR)
    hlt_ratio.append(hist_HLT_onhltptpt_lead_r)
    hlt_ratio.append(hist_HLT_onhltptpt_sublead_r)


    hlt_ratio.append(hist_m_onhltptprong)
    hlt_ratio.append(hist_m_onhltptrnn)
    hlt_ratio.append(hist_m_onhltptdeltaR)
    hlt_ratio.append(hist_m_onhltptpt_lead_r)
    hlt_ratio.append(hist_m_onhltptpt_sublead_r)  

    # ymax = hist_m_onhltptdeltaR.GetMaximum()
    # hist_HLT_onhltptdeltaR.GetYaxis().SetRangeUser(0, ymax*1.1)


    for i in range(5):
        hist_print_compare_ratio([hlt_ratio[i],
                            hlt_ratio[i+5]],
                ["HLTpt_r22", "HLTpt_Tau0+"],
                list_order[i], 0)
    
def Tau0_r22_eta( Tau0_root, r22_root):
    for k in range(len(kL)):
        if kL[k] == 1:
            inTau0 = ROOT.TFile.Open( Tau0_root ,"READ")
            inr22 = ROOT.TFile.Open( r22_root ,"READ")
    
    tree = inr22.Get("analysis")
    entries = range(tree.GetEntries())

###################################################################################
#TrigMatched_Taus_HLTetafl##########################################################

    hist_HLT_onhltetapt_lead_r = ROOT.TH1D("HLT_onhltetapt_lead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_HLT_onhltetapt_sublead_r = ROOT.TH1D("HLT_onhltetapt_sublead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_HLT_onhltetarnn = ROOT.TH1D("HLT_onhlteta_rnn","",50,0,1)
    hist_HLT_onhltetaprong = ROOT.TH1D("HLT_onhlteta_prong","",10,0,10)
    hist_HLT_onhltetadeltaR = ROOT.TH1D("HLT_onhltetadeltaR", "",50, -1, 4)

    # Manual Cut add later if necessary
    hist_m_onhltetapt_lead_r = ROOT.TH1D("m_onhltetapt_lead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_m_onhltetapt_sublead_r = ROOT.TH1D("m_onhltetapt_sublead_r","",r_pt[0],r_pt[1],r_pt[2])
    hist_m_onhltetarnn = ROOT.TH1D("m_onhlteta_rnn","",50,0,1)
    hist_m_onhltetaprong = ROOT.TH1D("m_onhlteta_prong","",10,0,10)
    hist_m_onhltetadeltaR = ROOT.TH1D("m_onhltetadeltaR", "",50, -1, 4)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_ETA25")
        HLT_1 = getattr(tree, "HLT_ETA25_Tau0") 
        if L1_1: 
            if HLT_1:
                for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                    if(i==0):
                        hist_HLT_onhltetapt_lead_r.Fill(
                                tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if(i==1):
                        hist_HLT_onhltetapt_sublead_r.Fill(
                            tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                        vec0= tree.TrigMatched_Taus_HLTetafl[0].Vect()
                        vec1= tree.TrigMatched_Taus_HLTetafl[1].Vect()
                        hist_HLT_onhltetadeltaR.Fill(vec1.DeltaR(vec0))  
                for j in range(len(tree.TrigMatched_rnn_HLTetafl)):
                    hist_HLT_onhltetarnn.Fill(tree.TrigMatched_rnn_HLTetafl[j],1)
                for k in range(len(tree.TrigMatched_prong_HLTetafl)):
                    hist_HLT_onhltetaprong.Fill(tree.TrigMatched_prong_HLTetafl[k], 1)
                    

    tree = inTau0.Get("analysis")
    entries = range(tree.GetEntries())

    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_ETA25")
        HLT_1 = getattr(tree, "HLT_ETA25_Tau0") 
        if L1_1:
            if HLT_1:
                if len(tree.TrigMatched_Taus_HLTetafl)<2 : continue
                for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                    if(i==0 and tree.TrigMatched_Taus_HLTetafl[0].Pt()>35
                        and tree.TrigMatched_Taus_HLTetafl[1].Pt()>25):
                        hist_m_onhltetapt_lead_r.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if(i==1 and tree.TrigMatched_Taus_HLTetafl[0].Pt()>35
                            and tree.TrigMatched_Taus_HLTetafl[1].Pt()>25):
                        hist_m_onhltetapt_sublead_r.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                        vec0= tree.TrigMatched_Taus_HLTetafl[0].Vect()
                        vec1= tree.TrigMatched_Taus_HLTetafl[1].Vect()
                        hist_m_onhltetadeltaR.Fill(vec1.DeltaR(vec0))  
                if(tree.TrigMatched_Taus_HLTetafl[0].Pt()>35
                    and tree.TrigMatched_Taus_HLTetafl[1].Pt()>25):
                    for j in range(len(tree.TrigMatched_rnn_HLTetafl)):
                        hist_m_onhltetarnn.Fill(tree.TrigMatched_rnn_HLTetafl[j],1)
                    for k in range(len(tree.TrigMatched_prong_HLTetafl)):
                        hist_m_onhltetaprong.Fill(tree.TrigMatched_prong_HLTetafl[k], 1)
######################################################################################

    hlt_ratio = []

    hlt_ratio.append(hist_HLT_onhltetaprong)
    hlt_ratio.append(hist_HLT_onhltetarnn)
    hlt_ratio.append(hist_HLT_onhltetadeltaR)
    hlt_ratio.append(hist_HLT_onhltetapt_lead_r)
    hlt_ratio.append(hist_HLT_onhltetapt_sublead_r)


    hlt_ratio.append(hist_m_onhltetaprong)
    hlt_ratio.append(hist_m_onhltetarnn)
    hlt_ratio.append(hist_m_onhltetadeltaR)
    hlt_ratio.append(hist_m_onhltetapt_lead_r)
    hlt_ratio.append(hist_m_onhltetapt_sublead_r)  

    # ymax = hist_m_onhltptdeltaR.GetMaximum()
    # hist_HLT_onhltptdeltaR.GetYaxis().SetRangeUser(0, ymax*1.1)


    for i in range(5):
        hist_print_compare_ratio([hlt_ratio[i],
                            hlt_ratio[i+5]],
                ["HLTeta_r22", "HLTeta_Tau0+"],
                list_order[i], 0)



def main(i):
    print(i)
    if (i=="1"): 
        Tau0_r22_pt( "Tau0_Pass.root", "r22_Pass.root")
    if (i=="2"): 
        Tau0_r22_eta( "Tau0_Pass.root", "r22_Pass.root")
    if (i=="3"): 
        Tau0_r22_pt( "Tau0_PassFail.root", "r22_PassFail.root")
    if (i=="4"): 
        Tau0_r22_eta( "Tau0_PassFail.root", "r22_PassFail.root")

if __name__ == "__main__" :
    print("Hello, Start Ploting for HLT Tau0-r22 study")
    main(sys.argv[1])
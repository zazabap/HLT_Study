# Author: Shiwen An 
# Date: 2022/08/01
# Purpose: Add some codes for emulation different part

import sys
from numpy import indices, size
from sympy import false, true
from torch import log2_
from HLT_Study import *
from L1_HLT_cut import *
from emulation import * 

taus = ["r22_Pass", "r22_PassFail", "Tau0_Pass", "Tau0_PassFail"]
list_order = ["RNN_Score","Prong","Delta_R","p_T","Subleading"]

r_pt = [100, 0, 250]

emu_order = [
    "Pt",
    "PtdR",
    "RNN",
    "Pt+RNN",
    "Pt+RNN+Delta_R"
]

#These cuts all work on pt only
def tree_online_pt_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        if ( tree.TrigMatched_Taus_HLTptfl[i].Pt() < 35): continue
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            if ( tree.TrigMatched_Taus_HLTptfl[j].Pt() < 25): continue
            indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
            indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())
    return indices
    
def tree_online_ptdR_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        if ( tree.TrigMatched_Taus_HLTptfl[i].Pt() < 35): continue
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            if ( tree.TrigMatched_Taus_HLTptfl[j].Pt() < 25): continue
            vec0 = tree.TrigMatched_Taus_HLTptfl[j].Vect()
            vec1 = tree.TrigMatched_Taus_HLTptfl[i].Vect()
            dR = vec0.DeltaR(vec1)
            if (  dR> 0.3 and dR <3.0) : 
                indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
                indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())
    return indices

def tree_online_RNN_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            pt0 = tree.TrigMatched_Taus_HLTptfl[j].Pt()
            pt1 = tree.TrigMatched_Taus_HLTptfl[i].Pt()
            rnn_m_0 = tree.TrigMatched_TauIDm_HLTptfl[j]
            rnn_m_1 = tree.TrigMatched_TauIDm_HLTptfl[i]
            rnn_l_0 = tree.TrigMatched_TauIDl_HLTptfl[j]
            rnn_l_1 = tree.TrigMatched_TauIDl_HLTptfl[i]
            rnn = rnn_region(pt0,pt1,rnn_m_0, rnn_m_1, rnn_l_0, rnn_l_1)
            if (rnn): 
                indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
                indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())
    return indices

def tree_online_dR_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            vec0 = tree.TrigMatched_Taus_HLTptfl[j].Vect()
            vec1 = tree.TrigMatched_Taus_HLTptfl[i].Vect()
            dR = vec0.DeltaR(vec1)
            if ( dR> 0.3 and dR <3.0) : 
                indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
                indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())           
    return indices 

def tree_online_RNNdR_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            vec0 = tree.TrigMatched_Taus_HLTptfl[j].Vect()
            vec1 = tree.TrigMatched_Taus_HLTptfl[i].Vect()
            pt0 = tree.TrigMatched_Taus_HLTptfl[j].Pt()
            pt1 = tree.TrigMatched_Taus_HLTptfl[i].Pt()
            rnn_m_0 = tree.TrigMatched_TauIDm_HLTptfl[j]
            rnn_m_1 = tree.TrigMatched_TauIDm_HLTptfl[i]
            rnn_l_0 = tree.TrigMatched_TauIDl_HLTptfl[j]
            rnn_l_1 = tree.TrigMatched_TauIDl_HLTptfl[i]
            rnn = rnn_region(pt0,pt1,rnn_m_0, rnn_m_1, rnn_l_0, rnn_l_1)
            if (rnn == false ): continue
            dR = vec0.DeltaR(vec1)
            if ( rnn and dR> 0.3 and dR <3.0) : 
                indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
                indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())        
    return indices    

def tree_online_ptRNN_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        if ( tree.TrigMatched_Taus_HLTptfl[i].Pt() < 35): continue
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            if ( tree.TrigMatched_Taus_HLTptfl[j].Pt() < 25): continue
            vec0 = tree.TrigMatched_Taus_HLTptfl[j].Vect()
            vec1 = tree.TrigMatched_Taus_HLTptfl[i].Vect()
            passPt = true
            pt0 = tree.TrigMatched_Taus_HLTptfl[j].Pt()
            pt1 = tree.TrigMatched_Taus_HLTptfl[i].Pt()
            rnn_m_0 = tree.TrigMatched_TauIDm_HLTptfl[j]
            rnn_m_1 = tree.TrigMatched_TauIDm_HLTptfl[i]
            rnn_l_0 = tree.TrigMatched_TauIDl_HLTptfl[j]
            rnn_l_1 = tree.TrigMatched_TauIDl_HLTptfl[i]
            rnn = rnn_region(pt0,pt1,rnn_m_0, rnn_m_1, rnn_l_0, rnn_l_1)
            if (rnn): 
                indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
                indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())
    return indices

def tree_online_ptRNNdR_i(tree):
    indices = set()
    for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
        if ( tree.TrigMatched_Taus_HLTptfl[i].Pt() < 35): continue
        for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if (i==j): continue
            if ( tree.TrigMatched_Taus_HLTptfl[j].Pt() < 25): continue
            vec0 = tree.TrigMatched_Taus_HLTptfl[j].Vect()
            vec1 = tree.TrigMatched_Taus_HLTptfl[i].Vect()
            passPt = true
            pt0 = tree.TrigMatched_Taus_HLTptfl[j].Pt()
            pt1 = tree.TrigMatched_Taus_HLTptfl[i].Pt()
            rnn_m_0 = tree.TrigMatched_TauIDm_HLTptfl[j]
            rnn_m_1 = tree.TrigMatched_TauIDm_HLTptfl[i]
            rnn_l_0 = tree.TrigMatched_TauIDl_HLTptfl[j]
            rnn_l_1 = tree.TrigMatched_TauIDl_HLTptfl[i]
            rnn = rnn_region(pt0,pt1,rnn_m_0, rnn_m_1, rnn_l_0, rnn_l_1)
            if (rnn): passPtRNN = true
            else: continue
            dR = vec0.DeltaR(vec1)
            if (  dR> 0.3 and dR <3.0) : 
                indices.add(tree.TrigMatched_Taus_HLTptfl[i].Pt())
                indices.add(tree.TrigMatched_Taus_HLTptfl[j].Pt())
    return indices

def emulation_passed_taus(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open(input_root, "READ")

    print("Start Looping ", taus[t])
    tree = inFile.Get("analysis")
    entries = range(tree.GetEntries())
    hltoff = []
####Off_Matched_Tau##################################################################################
    hist_offhltrnn = ROOT.TH1D("offhlt_rnn", "", 50, 0, 1)
    hist_offhltprong = ROOT.TH1D("offhlt_prong", "", 10, 0, 10)
    hist_offhltpt_r = ROOT.TH1D("offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_offhltpt_lead_r = ROOT.TH1D(
        "offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_offhltpt_sublead_r = ROOT.TH1D(
        "offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_offhltptdeltaR = ROOT.TH1D("offhltptdeltaR", "", 50, -1, 4)

    hist_m1_on_emu_rnn = ROOT.TH1D("m1_on_emu__rnn", "", 50, 0, 1)
    hist_m1_on_emu_prong = ROOT.TH1D("m1_on_emu__prong", "", 10, 0, 10)
    hist_m1_on_emu_pt_r = ROOT.TH1D(
        "m1_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m1_on_emu_pt_lead_r = ROOT.TH1D(
        "m1_on_emu_pt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m1_on_emu_pt_sublead_r = ROOT.TH1D(
        "m1_on_emu_pt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m1_on_emu_ptdeltaR = ROOT.TH1D("m1_on_emu_ptdeltaR", "", 50, -1, 4)

    hist_m2_on_emu_rnn = ROOT.TH1D("m2_on_emu__rnn", "", 50, 0, 1)
    hist_m2_on_emu_prong = ROOT.TH1D("m2_on_emu__prong", "", 10, 0, 10)
    hist_m2_on_emu_pt_r = ROOT.TH1D(
        "m2_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m2_on_emu_pt_lead_r = ROOT.TH1D(
        "m2_on_emu_pt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m2_on_emu_pt_sublead_r = ROOT.TH1D(
        "m2_on_emu_pt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m2_on_emu_ptdeltaR = ROOT.TH1D("m2_on_emu_ptdeltaR", "", 50, -1, 4)

    hist_m3_on_emu_rnn = ROOT.TH1D("m3_on_emu__rnn", "", 50, 0, 1)
    hist_m3_on_emu_prong = ROOT.TH1D("m3_on_emu__prong", "", 10, 0, 10)
    hist_m3_on_emu_pt_r = ROOT.TH1D(
        "m3_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m3_on_emu_pt_lead_r = ROOT.TH1D(
        "m3_on_emu_pt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m3_on_emu_pt_sublead_r = ROOT.TH1D(
        "m3_on_emu_pt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m3_on_emu_ptdeltaR = ROOT.TH1D("m3_on_emu_ptdeltaR", "", 50, -1, 4)

    hist_m4_on_emu_rnn = ROOT.TH1D("m4_on_emu__rnn", "", 50, 0, 1)
    hist_m4_on_emu_prong = ROOT.TH1D("m4_on_emu__prong", "", 10, 0, 10)
    hist_m4_on_emu_pt_r = ROOT.TH1D(
        "m4_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m4_on_emu_pt_lead_r = ROOT.TH1D(
        "m4_on_emu_pt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m4_on_emu_pt_sublead_r = ROOT.TH1D(
        "m4_on_emu_pt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m4_on_emu_ptdeltaR = ROOT.TH1D("m4_on_emu_ptdeltaR", "", 50, -1, 4)

    hist_HLT_offhltrnn = ROOT.TH1D("HLT_offhlt_rnn", "", 50, 0, 1)
    hist_HLT_offhltprong = ROOT.TH1D("HLT_offhlt_prong", "", 10, 0, 10)
    hist_HLT_offhltpt_r = ROOT.TH1D(
        "HLT_offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_lead_r = ROOT.TH1D(
        "HLT_offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_sublead_r = ROOT.TH1D(
        "HLT_offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltptdeltaR = ROOT.TH1D("HLT_offhltptdeltaR", "", 50, -1, 4)

    hist_m5_on_emu_pt_r = ROOT.TH1D(
        "m5_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m6_on_emu_pt_r = ROOT.TH1D(
        "m6_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_m7_on_emu_pt_r = ROOT.TH1D(
        "m7_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])

    hist_l1_on_emu_pt_r = ROOT.TH1D(
        "l1_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_l2_on_emu_pt_r = ROOT.TH1D(
        "l2_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_l3_on_emu_pt_r = ROOT.TH1D(
        "l3_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_l4_on_emu_pt_r = ROOT.TH1D(
        "l4_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_l5_on_emu_pt_r = ROOT.TH1D(
        "l5_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_l6_on_emu_pt_r = ROOT.TH1D(
        "l6_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_l7_on_emu_pt_r = ROOT.TH1D(
        "l7_on_emu_pt_r", "", r_pt[0], r_pt[1], r_pt[2])

    # Selection+ Selection Pass HLT
    denominator = 0 # entries (pass select + L1)
    numerator_emu = 0 # entries (pass selection + L1) + (emu/HLT [online taus])
    numerator_hlt =0  # entries (pass selection + L1) + (emu/HLT [online taus])

    numerator_1 = 0 # pt
    numerator_2 = 0 # ptdR
    numerator_3 = 0 # ptRNN
    numerator_4 = 0 # ptRNNdR

    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_J25")
        L1_2 = getattr(tree, "L1_ETA25")
        # Bit confused about this point of trigger use
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "r22_PassFail":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "Tau0_Pass":
            HLT_1 = getattr(tree, "HLT_J25_Tau0")
            HLT = "HLT_J25_Tau0"
        elif taus[t] == "Tau0_PassFail":
            HLT_1 = getattr(tree, "HLT_J25_Tau0")
            HLT = "HLT_J25_Tau0"

        # Selection
        select = True
        select = select and (len(tree.Offline_Matched_Taus) >= 2)
        if(select):
            select = select and (tree.Offline_Matched_Taus[0].Pt() > 20)
            select = select and (tree.Offline_Matched_Taus[1].Pt() > 12)
        if(len(tree.Off_Matched_TauIDl)<2): continue
        for i in range(len(tree.Off_Matched_TauIDl)):
                # print(tree.Off_Matched_TauIDl[i])
                if(tree.Off_Matched_TauIDl[0] == True
                 and tree.Off_Matched_TauIDl[1] == True):
                    select = select 
                else:
                    select = False
        select = select and (L1_1 or L1_2)

        # How to pass RNN loose ID?
        if(select):

            # indice
            i_pt = tree_online_pt_i(tree)
            i_ptdR = tree_online_ptdR_i(tree)
            i_ptRNN = tree_online_ptRNN_i(tree)
            i_ptRNNdR = tree_online_ptRNNdR_i(tree)

            i_dR = tree_online_dR_i(tree)
            i_RNN = tree_online_RNN_i(tree)
            i_RNNdR = tree_online_RNNdR_i(tree)

            for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                pt0 = tree.TrigMatched_Taus_HLTptfl[i].Pt()
                hist_offhltpt_r.Fill(pt0, 1)
                if(i == 0):
                    hist_offhltpt_lead_r.Fill(
                                tree.TrigMatched_Taus_HLTptfl[0].Pt(), 1)
                if(i == 1):
                    hist_offhltpt_sublead_r.Fill(
                                tree.TrigMatched_Taus_HLTptfl[1].Pt(), 1)
                    vec0 = tree.TrigMatched_Taus_HLTptfl[0].Vect()
                    vec1 = tree.TrigMatched_Taus_HLTptfl[1].Vect()
                    hist_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
            for j in range(len(tree.TrigMatched_rnn_HLTptfl)):
                    hist_offhltrnn.Fill(tree.TrigMatched_rnn_HLTptfl[j], 1)
            for k in range(len(tree.TrigMatched_prong_HLTptfl)):
                    hist_offhltprong.Fill(tree.TrigMatched_prong_HLTptfl[k], 1)  
            if L1_1: denominator = denominator+1
            if L1_1:
                if len(i_pt) > 0 : hist_l1_on_emu_pt_r.Fill(max(i_pt), 1)
                if len(i_ptdR) > 0 : hist_l2_on_emu_pt_r.Fill(max(i_ptdR), 1)
                if len(i_ptRNN) > 0 : hist_l3_on_emu_pt_r.Fill(max(i_ptRNN), 1)
                if len(i_ptRNNdR) > 0 : hist_l4_on_emu_pt_r.Fill(max(i_ptRNNdR), 1)
                if len(i_dR) > 0 : hist_l5_on_emu_pt_r.Fill(max(i_dR), 1)
                if len(i_RNN) > 0 : hist_l6_on_emu_pt_r.Fill(max(i_RNN), 1)
                if len(i_RNNdR) > 0 : hist_l7_on_emu_pt_r.Fill(max(i_RNNdR), 1)

                for i in i_pt:
                    hist_m1_on_emu_pt_r.Fill(i, 1)                
                for i in i_ptdR:
                    hist_m2_on_emu_pt_r.Fill(i, 1)
                for i in i_ptRNN:
                    hist_m3_on_emu_pt_r.Fill(i, 1)
                for i in i_ptRNNdR:
                    hist_m4_on_emu_pt_r.Fill(i, 1)
                for i in i_dR:
                    hist_m5_on_emu_pt_r.Fill(i, 1)
                for i in i_RNN:
                    hist_m6_on_emu_pt_r.Fill(i, 1)
                for i in i_RNNdR:
                    hist_m7_on_emu_pt_r.Fill(i, 1)

    print("Event level check")
    print("pt: ", numerator_1, "percentage: ", numerator_1/denominator )
    print("ptdR: ", numerator_2, "percentage: ", numerator_2/denominator)
    print("ptRNN: ", numerator_3, "percentage: ", numerator_3/denominator)
    print("ptRNNdR: ", numerator_4, "percentage: ", numerator_4/denominator)
    print("select: ", denominator)


    hltoff.append(hist_offhltrnn)
    hltoff.append(hist_offhltprong)
    hltoff.append(hist_offhltptdeltaR)
    hltoff.append(hist_offhltpt_r)
    hltoff.append(hist_offhltpt_sublead_r)


    hlt_pt_emu = []
    hlt_pt_emu.append(hist_offhltpt_r)
    hlt_pt_emu.append(hist_m1_on_emu_pt_r)
    hlt_pt_emu.append(hist_m2_on_emu_pt_r)
    hlt_pt_emu.append(hist_m3_on_emu_pt_r)
    hlt_pt_emu.append(hist_m4_on_emu_pt_r)

    hlt_emu = []
    hlt_emu.append(hist_offhltpt_r)
    hlt_emu.append(hist_m5_on_emu_pt_r)
    hlt_emu.append(hist_m6_on_emu_pt_r)
    hlt_emu.append(hist_m7_on_emu_pt_r)

    hlt_l_pt_emu = []
    hlt_l_pt_emu.append(hist_offhltpt_r)
    hlt_l_pt_emu.append(hist_l1_on_emu_pt_r)
    hlt_l_pt_emu.append(hist_l2_on_emu_pt_r)
    hlt_l_pt_emu.append(hist_l3_on_emu_pt_r)
    hlt_l_pt_emu.append(hist_l4_on_emu_pt_r)

    hlt_l_emu = []
    hlt_l_emu.append(hist_offhltpt_r)
    hlt_l_emu.append(hist_l5_on_emu_pt_r)
    hlt_l_emu.append(hist_l6_on_emu_pt_r)
    hlt_l_emu.append(hist_l7_on_emu_pt_r)

    # hist_print_compare(hlt_pt_emu,
    #         ["select", "pt", "ptdR", "ptRNN", "ptRNNdR"],
    #        "p_T", t)    

    # hist_print_compare(hlt_emu,
    #             ["select","dR", "RNN", "RNNdR"],
    #             "p_T", t)

    # hist_print_compare(hlt_l_pt_emu,
    #             ["select", "pt", "ptdR", "ptRNN", "ptRNNdR"],
    #                 "p_T", t)
    
    hist_print_compare(hlt_l_emu,
                ["select","dR", "RNN", "RNNdR"],
                "p_T", t)

    # hist_print_compare_ratio([hltoff[13], hltoff[3]],
    # ["ptdR", "select"], "p_T", t)

    # hist_print_compare_ratio([hltoff[18], hltoff[3]],
    # ["ptRNN", "select"], "p_T", t)
    
    # hist_print_compare_ratio([hltoff[23], hltoff[3]],
    # ["ptRNNdR", "select"], "p_T", t)

    # hist_print_compare_ratio([hltoff[18], hltoff[13]],
    # ["ptRNN", "ptdR"], "p_T", t)


def main(i):
    emulation_passed_taus("Tau0_PassFail.root", 3)
    


if __name__ == "__main__" :
    print("Hello, Start Plotting for Emulation study")
    emulation_passed_taus("Tau0_PassFail.root", 3)

    # main(sys.argv[1])
from xmlrpc.client import Fault
from sympy import false, true
from torch import log2_
from HLT_Study import *
from L1_HLT_cut import *

taus = ["r22_Pass", "r22_PassFail", "Tau0_Pass", "Tau0_PassFail"]
list_order = [
    "RNN_Score",
    "Prong",
    "Delta_R",
    "leading",
    "Subleading"
]

r_pt = [50, 0, 250]


def tree_loop_select_pt(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 10:
            inFile = ROOT.TFile.Open(input_root, "READ")
        # if kL[k] == 1:
        #     inFile = ROOT.TFile.Open(input_root, "READ")

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

    hist_HLT_offhltrnn = ROOT.TH1D("HLT_offhlt_rnn", "", 50, 0, 1)
    hist_HLT_offhltprong = ROOT.TH1D("HLT_offhlt_prong", "", 10, 0, 10)
    hist_HLT_offhltpt_r = ROOT.TH1D(
        "HLT_offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_lead_r = ROOT.TH1D(
        "HLT_offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_sublead_r = ROOT.TH1D(
        "HLT_offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltptdeltaR = ROOT.TH1D("HLT_offhltptdeltaR", "", 50, -1, 4)

    # Selection+ Selection Pass HLT
    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_J25")
        L1_2 = getattr(tree, "L1_ETA25")
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
            for i in range(len(tree.Offline_Matched_Taus)):
                hist_offhltpt_r.Fill(tree.Offline_Matched_Taus[i].Pt(), 1)
                if(i == 0):
                    hist_offhltpt_lead_r.Fill(
                        tree.Offline_Matched_Taus[0].Pt(), 1)
                if(i == 1):
                    hist_offhltpt_sublead_r.Fill(
                        tree.Offline_Matched_Taus[1].Pt(), 1)
                    vec0 = tree.Offline_Matched_Taus[0].Vect()
                    vec1 = tree.Offline_Matched_Taus[1].Vect()
                    hist_offhltptdeltaR.Fill(vec1.DeltaR(vec0))                    
            for j in range(len(tree.Off_Matched_TauRNN)):
                hist_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
            for k in range(len(tree.Off_Matched_TauProng)):
                hist_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

            if L1_1:
                if HLT_1:
                    for i in range(len(tree.Offline_Matched_Taus)):
                        hist_HLT_offhltpt_r.Fill(
                            tree.Offline_Matched_Taus[i].Pt(), 1)
                        if(i == 0):
                            hist_HLT_offhltpt_lead_r.Fill(
                                tree.Offline_Matched_Taus[0].Pt(), 1)
                        if(i == 1):
                            hist_HLT_offhltpt_sublead_r.Fill(
                                tree.Offline_Matched_Taus[1].Pt(), 1)
                            vec0 = tree.Offline_Matched_Taus[0].Vect()
                            vec1 = tree.Offline_Matched_Taus[1].Vect()
                            hist_HLT_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
                    for j in range(len(tree.Off_Matched_TauRNN)):
                        hist_HLT_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
                    for k in range(len(tree.Off_Matched_TauProng)):
                        hist_HLT_offhltprong.Fill(
                            tree.Off_Matched_TauProng[k], 1)

    hltoff.append(hist_offhltrnn)
    hltoff.append(hist_offhltprong)
    hltoff.append(hist_offhltptdeltaR)
    hltoff.append(hist_offhltpt_lead_r)
    hltoff.append(hist_offhltpt_sublead_r)

    hltoff.append(hist_HLT_offhltrnn)
    hltoff.append(hist_HLT_offhltprong)
    hltoff.append(hist_HLT_offhltptdeltaR)
    hltoff.append(hist_HLT_offhltpt_lead_r)
    hltoff.append(hist_HLT_offhltpt_sublead_r)

    for i in range(5):
        hist_print_compare_ratio_eff([hltoff[i],
                            hltoff[i+5]],
                ["Select", "HLT+Select"],
                list_order[i], t)

def tree_loop_eff_pt(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 10:
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

    hist_L1_offhltrnn = ROOT.TH1D("L1_offhlt_rnn", "", 50, 0, 1)
    hist_L1_offhltprong = ROOT.TH1D("L1_offhlt_prong", "", 10, 0, 10)
    hist_L1_offhltpt_r = ROOT.TH1D(
        "L1_offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_L1_offhltpt_lead_r = ROOT.TH1D(
        "L1_offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_L1_offhltpt_sublead_r = ROOT.TH1D(
        "L1_offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_L1_offhltptdeltaR = ROOT.TH1D("L1_offhltptdeltaR", "", 50, -1, 4)

    hist_HLT_offhltrnn = ROOT.TH1D("HLT_offhlt_rnn", "", 50, 0, 1)
    hist_HLT_offhltprong = ROOT.TH1D("HLT_offhlt_prong", "", 10, 0, 10)
    hist_HLT_offhltpt_r = ROOT.TH1D(
        "HLT_offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_lead_r = ROOT.TH1D(
        "HLT_offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_sublead_r = ROOT.TH1D(
        "HLT_offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltptdeltaR = ROOT.TH1D("HLT_offhltptdeltaR", "", 50, -1, 4)

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
            HLT = "HLT_J25_Tau0"
        elif taus[t] == "Tau0_PassFail":
            HLT_1 = getattr(tree, "HLT_J25_Tau0")
            HLT = "HLT_J25_Tau0"

        for i in range(len(tree.Offline_Matched_Taus)):
            hist_offhltpt_r.Fill(tree.Offline_Matched_Taus[i].Pt(), 1)
            if(i == 0):
                hist_offhltpt_lead_r.Fill(
                    tree.Offline_Matched_Taus[0].Pt(), 1)
            if(i == 1):
                hist_offhltpt_sublead_r.Fill(
                    tree.Offline_Matched_Taus[1].Pt(), 1)
                vec0 = tree.Offline_Matched_Taus[0].Vect()
                vec1 = tree.Offline_Matched_Taus[1].Vect()
                hist_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
        for j in range(len(tree.Off_Matched_TauRNN)):
            hist_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
        for k in range(len(tree.Off_Matched_TauProng)):
            hist_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

        # Should HLT be applied only after the L1 hardware trigger is passed?
        if L1_1:
            for i in range(len(tree.Offline_Matched_Taus)):
                hist_L1_offhltpt_r.Fill(
                    tree.Offline_Matched_Taus[i].Pt(), 1)
                if(i == 0):
                    hist_L1_offhltpt_lead_r.Fill(
                        tree.Offline_Matched_Taus[0].Pt(), 1)
                if(i == 1):
                    hist_L1_offhltpt_sublead_r.Fill(
                        tree.Offline_Matched_Taus[1].Pt(), 1)

                    vec0 = tree.Offline_Matched_Taus[0].Vect()
                    vec1 = tree.Offline_Matched_Taus[1].Vect()
                    hist_L1_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
            for j in range(len(tree.Off_Matched_TauRNN)):
                hist_L1_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
            for k in range(len(tree.Off_Matched_TauProng)):
                hist_L1_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

            if HLT_1:
                for i in range(len(tree.Offline_Matched_Taus)):
                    hist_HLT_offhltpt_r.Fill(
                        tree.Offline_Matched_Taus[i].Pt(), 1)
                    if(i == 0):
                        hist_HLT_offhltpt_lead_r.Fill(
                            tree.Offline_Matched_Taus[0].Pt(), 1)
                    if(i == 1):
                        hist_HLT_offhltpt_sublead_r.Fill(
                            tree.Offline_Matched_Taus[1].Pt(), 1)

                        vec0 = tree.Offline_Matched_Taus[0].Vect()
                        vec1 = tree.Offline_Matched_Taus[1].Vect()
                        hist_HLT_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
                for j in range(len(tree.Off_Matched_TauRNN)):
                    hist_HLT_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
                for k in range(len(tree.Off_Matched_TauProng)):
                    hist_HLT_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

    hltoff.append(hist_offhltrnn)
    hltoff.append(hist_offhltprong)
    hltoff.append(hist_offhltptdeltaR)
    hltoff.append(hist_offhltpt_lead_r)
    hltoff.append(hist_offhltpt_sublead_r)

    hltoff.append(hist_L1_offhltrnn)
    hltoff.append(hist_L1_offhltprong)
    hltoff.append(hist_L1_offhltptdeltaR)
    hltoff.append(hist_L1_offhltpt_lead_r)
    hltoff.append(hist_L1_offhltpt_sublead_r)

    hltoff.append(hist_HLT_offhltrnn)
    hltoff.append(hist_HLT_offhltprong)
    hltoff.append(hist_HLT_offhltptdeltaR)
    hltoff.append(hist_HLT_offhltpt_lead_r)
    hltoff.append(hist_HLT_offhltpt_sublead_r)

    for i in range(5):
        # posleg(leg_pos[i][0], leg_pos[i][1], leg_pos[i][2])
        hist_print_compare([hltoff[i],
                            hltoff[i+5],
                            hltoff[i+10]],
                           ["N/A", L1,  HLT],
                           list_order[i], t)
        a = [int(hltoff[i].GetEntries()),
             int(hltoff[i+5].GetEntries()),
             int(hltoff[i+10].GetEntries())]
        print("Efficiency HLT/L1", a[2]/a[1])
        b = [hltoff[i].GetName(),
             hltoff[i+5].GetName(),
             hltoff[i+10].GetName()]
        print("Efficiency "+b[2]+"HLT/ALL", a[2]/a[0])
        print("Efficiency "+b[2]+"HLT/L1", a[2]/a[1])


def tree_loop_eff_eta(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 10:
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

    hist_L1_offhltrnn = ROOT.TH1D("L1_offhlt_rnn", "", 50, 0, 1)
    hist_L1_offhltprong = ROOT.TH1D("L1_offhlt_prong", "", 10, 0, 10)
    hist_L1_offhltpt_r = ROOT.TH1D(
        "L1_offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_L1_offhltpt_lead_r = ROOT.TH1D(
        "L1_offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_L1_offhltpt_sublead_r = ROOT.TH1D(
        "L1_offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_L1_offhltptdeltaR = ROOT.TH1D("L1_offhltptdeltaR", "", 50, -1, 4)

    hist_HLT_offhltrnn = ROOT.TH1D("HLT_offhlt_rnn", "", 50, 0, 1)
    hist_HLT_offhltprong = ROOT.TH1D("HLT_offhlt_prong", "", 10, 0, 10)
    hist_HLT_offhltpt_r = ROOT.TH1D(
        "HLT_offhltpt_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_lead_r = ROOT.TH1D(
        "HLT_offhltpt_lead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltpt_sublead_r = ROOT.TH1D(
        "HLT_offhltpt_sublead_r", "", r_pt[0], r_pt[1], r_pt[2])
    hist_HLT_offhltptdeltaR = ROOT.TH1D("HLT_offhltptdeltaR", "", 50, -1, 4)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_ETA25")
        L1 = "L1_ETA25"
        # Bit confused about this point of trigger use
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_ETA25_r22")
            HLT = "HLT_ETA25_r22"
        elif taus[t] == "r22_PassFail":
            HLT_1 = getattr(tree, "HLT_ETA25_r22")
            HLT = "HLT_ETA25_r22"
        elif taus[t] == "Tau0_Pass":
            HLT_1 = getattr(tree, "HLT_ETA25_Tau0")
            HLT = "HLT_ETA25_Tau0"
        elif taus[t] == "Tau0_PassFail":
            HLT_1 = getattr(tree, "HLT_ETA25_Tau0")
            HLT = "HLT_ETA25_Tau0"

        for i in range(len(tree.Offline_Matched_Taus)):
            hist_offhltpt_r.Fill(tree.Offline_Matched_Taus[i].Pt(), 1)
            if(i == 0):
                hist_offhltpt_lead_r.Fill(
                    tree.Offline_Matched_Taus[0].Pt(), 1)
            if(i == 1):
                hist_offhltpt_sublead_r.Fill(
                    tree.Offline_Matched_Taus[1].Pt(), 1)
                vec0 = tree.Offline_Matched_Taus[0].Vect()
                vec1 = tree.Offline_Matched_Taus[1].Vect()
                hist_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
        for j in range(len(tree.Off_Matched_TauRNN)):
            hist_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
        for k in range(len(tree.Off_Matched_TauProng)):
            hist_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

        # Should HLT be applied only after the L1 hardware trigger is passed?
        if L1_1:
            for i in range(len(tree.Offline_Matched_Taus)):
                hist_L1_offhltpt_r.Fill(
                    tree.Offline_Matched_Taus[i].Pt(), 1)
                if(i == 0):
                    hist_L1_offhltpt_lead_r.Fill(
                        tree.Offline_Matched_Taus[0].Pt(), 1)
                if(i == 1):
                    hist_L1_offhltpt_sublead_r.Fill(
                        tree.Offline_Matched_Taus[1].Pt(), 1)

                    vec0 = tree.Offline_Matched_Taus[0].Vect()
                    vec1 = tree.Offline_Matched_Taus[1].Vect()
                    hist_L1_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
            for j in range(len(tree.Off_Matched_TauRNN)):
                hist_L1_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
            for k in range(len(tree.Off_Matched_TauProng)):
                hist_L1_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

            if HLT_1:
                for i in range(len(tree.Offline_Matched_Taus)):
                    hist_HLT_offhltpt_r.Fill(
                        tree.Offline_Matched_Taus[i].Pt(), 1)
                    if(i == 0):
                        hist_HLT_offhltpt_lead_r.Fill(
                            tree.Offline_Matched_Taus[0].Pt(), 1)
                    if(i == 1):
                        hist_HLT_offhltpt_sublead_r.Fill(
                            tree.Offline_Matched_Taus[1].Pt(), 1)

                        vec0 = tree.Offline_Matched_Taus[0].Vect()
                        vec1 = tree.Offline_Matched_Taus[1].Vect()
                        hist_HLT_offhltptdeltaR.Fill(vec1.DeltaR(vec0))
                for j in range(len(tree.Off_Matched_TauRNN)):
                    hist_HLT_offhltrnn.Fill(tree.Off_Matched_TauRNN[j], 1)
                for k in range(len(tree.Off_Matched_TauProng)):
                    hist_HLT_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

    hltoff.append(hist_offhltrnn)
    hltoff.append(hist_offhltprong)
    hltoff.append(hist_offhltptdeltaR)
    hltoff.append(hist_offhltpt_lead_r)
    hltoff.append(hist_offhltpt_sublead_r)

    hltoff.append(hist_L1_offhltrnn)
    hltoff.append(hist_L1_offhltprong)
    hltoff.append(hist_L1_offhltptdeltaR)
    hltoff.append(hist_L1_offhltpt_lead_r)
    hltoff.append(hist_L1_offhltpt_sublead_r)

    hltoff.append(hist_HLT_offhltrnn)
    hltoff.append(hist_HLT_offhltprong)
    hltoff.append(hist_HLT_offhltptdeltaR)
    hltoff.append(hist_HLT_offhltpt_lead_r)
    hltoff.append(hist_HLT_offhltpt_sublead_r)

    for i in range(5):
        # posleg(leg_pos[i][0], leg_pos[i][1], leg_pos[i][2])
        hist_print_compare([hltoff[i],
                            hltoff[i+5],
                            hltoff[i+10]],
                           ["N/A", L1,  HLT],
                           list_order[i], t)
        a = [int(hltoff[i].GetEntries()),
             int(hltoff[i+5].GetEntries()),
             int(hltoff[i+10].GetEntries())]
        print("Efficiency HLT/L1", a[2]/a[1])
        b = [hltoff[i].GetName(),
             hltoff[i+5].GetName(),
             hltoff[i+10].GetName()]
        print("Efficiency "+b[2]+"HLT/ALL", a[2]/a[0])
        print("Efficiency "+b[2]+"HLT/L1", a[2]/a[1])


def offline_efficiency(input_root, t):
    print("Offline Efficiency calculation based on HLT")


def main():
    # tree_loop_eff_pt("r22_Pass.root", 0)
    # tree_loop_eff_pt("r22_PassFail.root", 1)
    # tree_loop_eff_pt("Tau0_Pass.root", 2)
    # tree_loop_eff_pt("Tau0_PassFail.root", 3)

    # tree_loop_eff_eta( "r22_Pass.root", 0)
    # tree_loop_eff_eta("r22_PassFail.root", 1)
    # tree_loop_eff_eta("Tau0_Pass.root", 2)
    # tree_loop_eff_eta("Tau0_PassFail.root", 3)

    # tree_loop_select_pt("r22_Pass.root", 0)
    tree_loop_select_pt("r22_PassFail.root", 1)
    # tree_loop_select_pt("Tau0_Pass.root", 2)
    tree_loop_select_pt("Tau0_PassFail.root", 3)


if __name__ == "__main__":
    print("Hello, Start Ploting for HLT")
    main()

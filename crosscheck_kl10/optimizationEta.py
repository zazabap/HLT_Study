from concurrent.futures import thread
from emulationEta import *
from HLT_Study import *

taus = ["r22_Pass", "r22_PassFail", "Tau0_Pass", "Tau0_PassFail"]

r_pt = [100, 0, 250]

emu_order = [
    "Pt",
    "PtdR",
    "RNN",
    "Pt+RNN",
    "Pt+RNN+Delta_R"
]

def PtHLT_threshold(tree):
    p1 = [false, false, false]
    threshold = [ (35, 15), (35, 20), (35, 25)]
    threshold = [ (50, 15), (50, 20), (50, 25)]

    c = 0

    for lead, sublead in threshold:
        for i in range(len(tree.TrigMatched_Taus_HLTetafl)) :
            if ( tree.TrigMatched_Taus_HLTetafl[i].Pt() < lead): continue
            for  j in range(len(tree.TrigMatched_Taus_HLTetafl)) :
                if (i==j): continue
                if ( tree.TrigMatched_Taus_HLTetafl[j].Pt() < sublead): continue
                p1[c] =true
        c = c+1
    return p1 

def PtRNNdR_threshold(tree):
    p1 = [false, false, false,
          false, false, false, 
          false, false, false]
    threshold = [ (25, 15), (30, 15), (35, 15),
                  (25, 20), (30, 20), (35, 20),   
                  (25, 25), (30, 25), (35, 25)]
    # threshold = [ (40, 15), (45, 15), (50, 15),
    #               (40, 20), (45, 20), (50, 20),   
    #               (40, 25), (45, 25), (50, 25)]
    c = 0
    for lead, sublead in threshold:
        for i in range(len(tree.TrigMatched_Taus_HLTetafl)) :
            if ( tree.TrigMatched_Taus_HLTetafl[i].Pt() < lead): continue
            for  j in range(len(tree.TrigMatched_Taus_HLTetafl)) :
                if (i==j): continue
                if ( tree.TrigMatched_Taus_HLTetafl[j].Pt() < sublead): continue
                vec0 = tree.TrigMatched_Taus_HLTetafl[j].Vect()
                vec1 = tree.TrigMatched_Taus_HLTetafl[i].Vect()
                pt0 = tree.TrigMatched_Taus_HLTetafl[j].Pt()
                pt1 = tree.TrigMatched_Taus_HLTetafl[i].Pt()
                rnn_m_0 = tree.TrigMatched_TauIDm_HLTetafl[j]
                rnn_m_1 = tree.TrigMatched_TauIDm_HLTetafl[i]
                rnn_l_0 = tree.TrigMatched_TauIDl_HLTetafl[j]
                rnn_l_1 = tree.TrigMatched_TauIDl_HLTetafl[i]
                rnn = rnn_region(pt0,pt1,rnn_m_0, rnn_m_1, rnn_l_0, rnn_l_1)
                if (rnn): passPtRNN = true
                else: continue
                dR = vec0.DeltaR(vec1)
                if (  dR> 0.3 ) : p1[c] =true
        c = c+1
    return p1 

def threshold_optimization_emu(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open(input_root, "READ")

    print("Start Looping ", taus[t])
    tree = inFile.Get("analysis")
    entries = range(tree.GetEntries())


    # Selection+ Selection Pass HLT
    denominator = 0 # entries (pass select + L1)
    numerator_emu = 0 # entries (pass selection + L1) + (emu/HLT [online taus])
    numerator_hlt =0  # entries (pass selection + L1) + (emu/HLT [online taus])

    numerator_1 = 0 # 25 15
    numerator_2 = 0 # 30 15
    numerator_3 = 0 # 35 15
    numerator_4 = 0 # 25 20 
    numerator_5 = 0 # 30 20 
    numerator_6 = 0 # 35 20 
    numerator_7 = 0 # 25 25
    numerator_8 = 0 # 30 25
    numerator_9 = 0 # 35 25


    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_ETA25")
        L1_2 = getattr(tree, "L1_J25")
        # Bit confused about this point of trigger use
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_ETA25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "r22_PassFail":
            HLT_1 = getattr(tree, "HLT_ETA25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "Tau0_Pass":
            HLT_1 = getattr(tree, "HLT_ETA25_Tau0")
            HLT = "HLT_J25_Tau0"
        elif taus[t] == "Tau0_PassFail":
            HLT_1 = getattr(tree, "HLT_ETA25_Tau0")
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
        # select = select and (L1_1 or L1_2)

        # How to pass RNN loose ID?
        if(select): 
            denominator = denominator+1
            if L1_1:
                p1 = PtRNNdR_threshold(tree)
                if p1[0] : numerator_1 = numerator_1 + 1
                if p1[1] : numerator_2 = numerator_2 + 1
                if p1[2] : numerator_3 = numerator_3 + 1
                if p1[3] : numerator_4 = numerator_4 + 1
                if p1[4] : numerator_5 = numerator_5 + 1
                if p1[5] : numerator_6 = numerator_6 + 1
                if p1[6] : numerator_7 = numerator_7 + 1
                if p1[7] : numerator_8 = numerator_8 + 1
                if p1[8] : numerator_9 = numerator_9 + 1

    print("Event level check ptRNNdR")
    print("25 15", numerator_1, "percentage: ", numerator_1/denominator)
    print("30 15", numerator_2, "percentage: ", numerator_2/denominator)
    print("35 15", numerator_3, "percentage: ", numerator_3/denominator)
    print("25 20", numerator_4, "percentage: ", numerator_4/denominator)
    print("30 20", numerator_5, "percentage: ", numerator_5/denominator)
    print("35 20", numerator_6, "percentage: ", numerator_6/denominator)
    print("25 25", numerator_7, "percentage: ", numerator_7/denominator)
    print("30 25", numerator_8, "percentage: ", numerator_8/denominator)
    print("35 25", numerator_9, "percentage: ", numerator_9/denominator)


def threshold_optimization_hlt(input_root, t):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open(input_root, "READ")

    print("Start Looping ", taus[t])
    tree = inFile.Get("analysis")
    entries = range(tree.GetEntries())

    # Selection+ Selection Pass HLT
    denominator = 0 # entries (pass select + L1)
    numerator_hlt =0  # entries (pass selection + L1) + (emu/HLT [online taus])
    numerator_hlt_check = 0 # entry checks before plot
    numerator_1 = 0
    numerator_2 = 0
    numerator_3 = 0

    for entry in entries:
        tree.GetEntry(entry)
        L1_1 = getattr(tree, "L1_ETA25")
        L1_2 = getattr(tree, "L1_J25")
        # Bit confused about this point of trigger use
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_ETA25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "r22_PassFail":
            HLT_1 = getattr(tree, "HLT_ETA25_r22")
            HLT = "HLT_J25_r22"
        elif taus[t] == "Tau0_Pass":
            HLT_1 = getattr(tree, "HLT_ETA25_Tau0")
            HLT = "HLT_J25_Tau0"
        elif taus[t] == "Tau0_PassFail":
            HLT_1 = getattr(tree, "HLT_ETA25_Tau0")
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

        if(select):
            if L1_1: denominator = denominator+1
            if L1_1 and HLT_1:
                p1 = PtHLT_threshold(tree)
                if p1[0] : numerator_1 = numerator_1 + 1
                if p1[1] : numerator_2 = numerator_2 + 1
                if p1[2] : numerator_3 = numerator_3 + 1
                
    print("35 15", numerator_1, "percentage: ", numerator_1/denominator )
    print("35 20", numerator_2, "percentage: ", numerator_2/denominator)
    print("35 25", numerator_3, "percentage: ", numerator_3/denominator)

if __name__ == "__main__" :
    print("Hello, Start Optimization Symmetric Option")
    # threshold_optimization_hlt("Tau0_Pass.root",2)
    threshold_optimization_emu( "Tau0_PassFail.root", 3)

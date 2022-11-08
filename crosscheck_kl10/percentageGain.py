# Author: Shiwen An 
# Date: 2022 08 22
# Purpose: Add some plots for optimization

# from asyncio.windows_events import NULL
import pandas as pd
from array import array
from optimization import *

def PtRNNdR_threshold_percentage(tree):
    p1 = [false, false, false,
          false, false, false, 
          false, false, false,
          false, false, false,
          false, false, false, 
          false, false, false]

    threshold = [ (25, 15), (30, 15), (35, 15),
                  (25, 20), (30, 20), (35, 20),   
                  (25, 25), (30, 25), (35, 25),
                  (40, 15), (45, 15), (50, 15),
                  (40, 20), (45, 20), (50, 20),   
                  (40, 25), (45, 25), (50, 25)]
    c = 0
    for lead, sublead in threshold:
        for i in range(len(tree.TrigMatched_Taus_HLTptfl)) :
            if ( tree.TrigMatched_Taus_HLTptfl[i].Pt() < lead): continue
            for  j in range(len(tree.TrigMatched_Taus_HLTptfl)) :
                if (i==j): continue
                if ( tree.TrigMatched_Taus_HLTptfl[j].Pt() < sublead): continue
                vec0 = tree.TrigMatched_Taus_HLTptfl[j].Vect()
                vec1 = tree.TrigMatched_Taus_HLTptfl[i].Vect()
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
                if (  dR> 0.3 and dR<3.0 ) : p1[c] =true
        c = c+1
    return p1 

def percentage_emu(input_root, t):
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

    numerators = [0,0,0,
                  0,0,0,
                  0,0,0,
                  0,0,0,
                  0,0,0,
                  0,0,0]

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
            if L1_1: denominator = denominator+1
            if L1_1:
                p1 = PtRNNdR_threshold_percentage(tree)
                for i_n in range(18):
                    if p1[i_n] : numerators[i_n] = numerators[i_n] +1


    print("Event level check ptRNNdR")

    threshold = [ (25, 15), (30, 15), (35, 15),
                  (25, 20), (30, 20), (35, 20),   
                  (25, 25), (30, 25), (35, 25),
                  (40, 15), (45, 15), (50, 15),
                  (40, 20), (45, 20), (50, 20),   
                  (40, 25), (45, 25), (50, 25)]
    c = 0
    for lead, sublead in threshold:
        print("lead: ", lead, "sublead: ", sublead, "percentage: ", numerators[c]/denominator)
        c = c+1

    plot_percentage(numerators, denominator)
    

def plot_percentage(numerators, denominator):
    x = array('d')
    y = array('d')
    y1 = array('d')
    y2 = array('d')

    denominator = numerators[8]

    x1 = [25, 30, 35, 40, 45, 50]
    x2 = [1123,2123,3123,4312,5123,6123]

    x1 = [25, 30, 35, 40, 45, 50]
    x2 = [numerators[6]/denominator,numerators[7]/denominator, numerators[8]/denominator,
         numerators[15]/denominator,numerators[16]/denominator, numerators[17]/denominator]
    x3 = [numerators[3]/denominator,numerators[4]/denominator, numerators[5]/denominator,
         numerators[12]/denominator,numerators[13]/denominator, numerators[14]/denominator]
    x4 = [numerators[0]/denominator,numerators[1]/denominator, numerators[2]/denominator,
         numerators[9]/denominator,numerators[10]/denominator, numerators[11]/denominator]

    for i in range(6):
        x.append(x1[i])
        y.append(x2[i])
        y1.append(x3[i])
        y2.append(x4[i])

    print(x)
    print(y)

    c1 = ROOT.TCanvas( 'c1', 'Percentage Gain', 400, 20, 1400, 1000 )
    c1.SetGrid()

    print("Obtain values here.")

    gr2 = ROOT.TGraph(6, x, y2)
    gr2.SetMarkerSize(2)
    gr2.SetMarkerColor( 2 )
    gr2.SetMarkerStyle( 23 )
    gr2.GetYaxis().SetTitle( 'Ratio' )
    gr2.GetXaxis().SetTitle( 'Leading p_{T}^{#tau} (GeV)')
    gr2.Draw("APL")

    gr1 = ROOT.TGraph(6, x, y1)
    gr1.SetMarkerSize(2)
    gr1.SetMarkerColor( 3 )
    gr1.SetMarkerStyle( 22 )
    gr1.Draw("CP")

    gr = ROOT.TGraph(6, x, y)
    gr.SetMarkerSize(2)
    gr.SetMarkerColor( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'a simple graph' )
    gr.Draw( 'CP' )
    gr2.GetYaxis().SetRangeUser(0.8,1.2)

    x_35_25 = array('d')
    x_35_25.append(35)
    y_35_25 = array('d')
    y_35_25.append(1)
    gr0 = ROOT.TGraph(1, x_35_25, y_35_25)
    gr0.SetMarkerSize(2.4)
    gr0.SetMarkerColor( 7 )
    gr0.SetMarkerStyle( 20 )
    gr0.Draw("P")    

    posleg("R","U",2)
    legend = ROOT.TLegend(0.7, 0.8, 0.95, 0.95)
    legend.SetTextSize(0.035)
    legend.SetBorderSize(0)
    legend.SetHeader("kl=10 subleading p_{T}^{#tau}")
    legend.AddEntry(gr, "25 GeV")
    legend.AddEntry(gr1,"20 GeV")
    legend.AddEntry(gr2,"15 GeV")
    legend.AddEntry(gr0,"Base")
    legend.Draw("same")

    c1.Update()
    c1.Print("test.png")

def plot_rate_plus(n1, n2):
    x_40_20 = array('d')
    x_30_25 = array('d')
    x_25_25 = array('d')
    x_35_20 = array('d')
    x_30_20 = array('d')
    x_25_20 = array('d')

    y_40_20 = array('d')
    y_30_25 = array('d')
    y_25_25 = array('d')
    y_35_20 = array('d')
    y_30_20 = array('d')
    y_25_20 = array('d')

    x_40_20.append(n1[12]*100)
    x_30_25.append(n1[7]*100)
    x_25_25.append(n1[6]*100)
    x_35_20.append(n1[5]*100)
    x_30_20.append(n1[4]*100)
    x_25_20.append(n1[3]*100)

    # Trigger with BDT
    # y_40_20.append(53.3405)
    # y_30_25.append(57.3348)
    # y_25_25.append(58.9265)
    # y_35_20.append(67.6334)
    # y_30_20.append(81.2624)
    # y_25_20.append(83.6999)

    # Trigger w/o BDT 
    y_40_20.append(51.2268)
    y_30_25.append(55.3923)
    y_25_25.append(57.3336)
    y_35_20.append(64.6538)
    y_30_20.append(76.9000)
    y_25_20.append(79.6872)


    c2 = ROOT.TCanvas( 'c2', 'Rate Efficiency', 400, 20, 1400, 1000 )
    # c2.SetGrid()

    print("Obtain Rate and plot efficiency here.")

    gr1 = ROOT.TGraph(1, x_40_20, y_40_20)
    gr1.SetMarkerSize(2.4)
    gr1.SetMarkerColor( 2 )
    gr1.SetMarkerStyle( 23 )
    gr1.GetYaxis().SetTitleOffset(1.0)
    gr1.GetYaxis().SetTitle( 'Rate [Hz] at 2e34' )
    gr1.GetXaxis().SetTitle( 'kl=10 Signal Efficiency [%]')
    gr1.GetYaxis().SetRangeUser(0, 100)
    gr1.Draw("AP")

    gr3 = ROOT.TGraph(1, x_35_20, y_35_20)
    gr3.SetMarkerSize(2.4)
    gr3.SetMarkerColor( 2 )
    gr3.SetMarkerStyle( 24 )
    gr3.Draw("P")

    gr4 = ROOT.TGraph(1, x_30_20, y_30_20)
    gr4.SetMarkerSize(2.4)
    gr4.SetMarkerColor( 2 )
    gr4.SetMarkerStyle( 25 )
    gr4.Draw("P")

    gr5 = ROOT.TGraph(1, x_25_20, y_25_20)
    gr5.SetMarkerSize(2.4)
    gr5.SetMarkerColor( 2 )
    gr5.SetMarkerStyle( 26 )
    gr5.Draw("P")

    gr2 = ROOT.TGraph(1, x_25_25, y_25_25)
    gr2.SetMarkerSize(2.4)
    gr2.SetMarkerColor( 2 )
    gr2.SetMarkerStyle( 22 )
    gr2.Draw("P")

    gr6 = ROOT.TGraph(1, x_30_25, y_30_25)
    gr6.SetMarkerSize(2.4)
    gr6.SetMarkerColor( 2 )
    gr6.SetMarkerStyle( 27 )
    gr6.Draw("P")


    x__40_20 = array('d')
    x__30_25 = array('d')
    x__25_25 = array('d')
    x__35_20 = array('d')
    x__30_20 = array('d')
    x__25_20 = array('d')

    y__40_20 = array('d')
    y__30_25 = array('d')
    y__25_25 = array('d')
    y__35_20 = array('d')
    y__30_20 = array('d')
    y__25_20 = array('d')

    x__40_20.append(n2[12]*100)
    x__30_25.append(n2[7]*100)
    x__25_25.append(n2[6]*100)
    x__35_20.append(n2[5]*100)
    x__30_20.append(n2[4]*100)
    x__25_20.append(n2[3]*100)

    # y__40_20.append(26.7306)
    # y__30_25.append(27.0895)
    # y__25_25.append(27.9940)
    # y__35_20.append(33.5199)
    # y__30_20.append(38.4038)
    # y__25_20.append(40.3331)

    y__40_20.append(25.1086)
    y__30_25.append(27.0895)
    y__25_25.append(27.9940)
    y__35_20.append(31.5399)
    y__30_20.append(36.4036)
    y__25_20.append(38.4986)

    grr1 = ROOT.TGraph(1, x__40_20, y__40_20)
    grr1.SetMarkerSize(2.4)
    grr1.SetMarkerColor( 4 )
    grr1.SetMarkerStyle( 23 )
    grr1.Draw("P")

    grr3 = ROOT.TGraph(1, x__35_20, y__35_20)
    grr3.SetMarkerSize(2.4)
    grr3.SetMarkerColor( 4 )
    grr3.SetMarkerStyle( 24 )
    grr3.Draw("P")

    grr4 = ROOT.TGraph(1, x__30_20, y__30_20)
    grr4.SetMarkerSize(2.4)
    grr4.SetMarkerColor( 4 )
    grr4.SetMarkerStyle( 25 )
    grr4.Draw("P")

    grr5 = ROOT.TGraph(1, x__25_20, y__25_20)
    grr5.SetMarkerSize(2.4)
    grr5.SetMarkerColor( 4 )
    grr5.SetMarkerStyle( 26 )
    grr5.Draw("P")

    grr2 = ROOT.TGraph(1, x__25_25, y__25_25)
    grr2.SetMarkerSize(2.4)
    grr2.SetMarkerColor( 4 )
    grr2.SetMarkerStyle( 22 )
    grr2.Draw("P")

    grr6 = ROOT.TGraph(1, x__30_25, y__30_25)
    grr6.SetMarkerSize(2.4)
    grr6.SetMarkerColor( 4 )
    grr6.SetMarkerStyle( 27 )
    grr6.Draw("P")
    
    # Current or execptional

    x_35_25 = array('d')
    x_35_25.append(n1[8]*100)
    y_35_25 = array('d')
    y_35_25.append(48.1304)

    x__35_25 = array('d')
    x__35_25.append(n2[8]*100)
    y__35_25 = array('d')
    y__35_25.append(23.8455)

    gr0 = ROOT.TGraph(1, x_35_25, y_35_25)
    gr0.SetMarkerSize(2.4)
    gr0.SetMarkerColor( 6 )
    gr0.SetMarkerStyle( 20 )
    gr0.Draw("P")

    grr0 = ROOT.TGraph(1, x__35_25, y__35_25)
    grr0.SetMarkerSize(2.4)
    grr0.SetMarkerColor( 7 )
    grr0.SetMarkerStyle( 20 )
    grr0.Draw("P")

    # gr = ROOT.TGraph(6, x, y)
    # gr.SetMarkerColor( 4 )
    # gr.SetMarkerStyle( 21 )
    # gr.SetTitle( 'a simple graph' )
    # gr.Draw( 'CP' )

    # gr1.GetXaxis().SetLimits(0.65*100, 0.77*100)
    gr1.GetXaxis().SetLimits(0.58*100, 0.68*100)
    gr1.GetYaxis().SetLimits(0, 100)
    
    posleg("L","U",2)

    legend0 =  ROOT.TLegend(0.3, 0.8, 0.4, 0.95)
    legend0.SetTextSize(0.025)
    legend0.SetBorderSize(0)
    legend0.AddEntry(0,"#splitline{Trigger chain: HLT_tauX_mediumRNN_tracktwoMVA_}{tauY_mediumRNN_tracktwoMVA_03dRAB}")
    # legend0.AddEntry(0,"")
    legend0.AddEntry(0,"#splitline{Red: L1_DR-TAU20ITAU12I-J25}{Blue: L1_TAU20IM_2TAU12IM_4J12p0ETA25}")
    # legend0.AddEntry(0,"")
    legend0.Draw("same")
                             
    legend1 = ROOT.TLegend(0.2, 0.7, 0.3, 0.95)
    legend1.SetTextSize(0.030)
    legend1.SetBorderSize(0)
    # legend1.SetHeader("J25")
    # legend.AddEntry(gr, "25 GeV")
    legend1.AddEntry(gr1,"40 20")
    legend1.AddEntry(gr3,"35 20")
    legend1.AddEntry(gr4,"30 20")
    legend1.AddEntry(gr5,"25 20")
    legend1.AddEntry(gr0,"35 25")
    legend1.AddEntry(gr6,"30 25")
    legend1.AddEntry(gr2,"25 25")    
    legend1.Draw("same")

    # legend = ROOT.TLegend(0.3, 0.7, 0.4, 0.95)
    # legend.SetTextSize(0.030)
    # legend.SetBorderSize(0)
    # legend.SetHeader("")
    # # legend.AddEntry(gr, "25 GeV")
    # legend.SetHeader("ETA25")
    # legend.AddEntry(grr1,"40 20")
    # legend.AddEntry(grr3,"35 20")
    # legend.AddEntry(grr4,"30 20")
    # legend.AddEntry(grr5,"25 20")
    # legend.AddEntry(grr0,"35 25")
    # legend.AddEntry(grr6,"30 25")
    # legend.AddEntry(grr2,"25 25")
    # legend.Draw("same")

    c2.Update()
    c2.Print("rate_pt_update_kl10.png")


def test():
    df = pd.read_csv("signalEfficiency.csv")
    print(df)
    df.replace(',', '', regex=True,inplace=True)

    numerators = [0.7629384703852788,
                  0.7615008625646924,
                  0.7520126509488212,
                  0.753737780333525,
                  0.7524439332949971,
                  0.7430994824611846,
                  0.6946520989074181,
                  0.6937895342150662,
                  0.6855951696377228,
                  0.7367740080506038,
                  0.7127659574468085,
                  0.6779758481886141,
                  0.7281483611270846,
                  0.7045715928694652,
                  0.6702127659574468,
                  0.6728004600345026,
                  0.6528177113283496,
                  0.6217653824036803]
    n1 = df['ptkl1'].to_numpy()
    n2 = df['etakl1'].to_numpy()
    n3 = df['ptkl10'].to_numpy()
    n4 = df['etakl10'].to_numpy()

    # n3 = pd.to_numeric(df['ptkl10'])
    # n4 = pd.to_numeric(df['etakl10'])

    # plot_percentage(n3, numerators[9])
    # plot_percentage(n4, numerators[9])
    # plot_rate_plus(n1, n2)

    plot_rate_plus(n3, n4)


if __name__ == "__main__" :
    print("Hello, Start Optimization Symmetric Option")
    test()
    # threshold_optimization_hlt("Tau0_Pass.root",2)
    # percentage_emu("Tau0_PassFail.root", 3)
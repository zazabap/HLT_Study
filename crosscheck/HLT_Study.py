

# Author: Shiwen An 
# Date: 2022/05/24
# Purpose: Crosscheck 
# More deteailed work 
# with better plots

#!/usr/bin/env python
#Version 22.05.10.11.00
import math
import ROOT
import ast
from ast import Add, BinOp, Num
ROOT.gROOT.SetBatch(True)
ROOT.gROOT.SetStyle("ATLAS")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetErrorX()
ROOT.gStyle.SetMarkerStyle(1)
ROOT.gStyle.SetTitleOffset(1.05,"X")
ROOT.gStyle.SetPadLeftMargin(0.125)
ROOT.gStyle.SetPadRightMargin(0.03)
ROOT.gStyle.SetPadTopMargin(0.025)
ROOT.gStyle.SetPadBottomMargin(0.125)
ROOT.gStyle.SetPalette(1)
ROOT.gROOT.ForceStyle()

taus = ["passfail","pass"]
taus = ["r22_Pass", "r22_PassFail", "Tau0_Pass", "Tau0_PassFail"]
color = [ROOT.kBlack, ROOT.kRed, ROOT.kBlue, ROOT.kGreen]
kL = [1,10]
kL = [1]
printer = 5000;

def posleg(pos_x, pos_y, items):
    global l_x_min, l_x_max, l_y_min, l_y_max
    width_x = 0.275; depth_i = 0.05;
    l_x_L = 0.145; l_x_R = 0.95; l_x_C = (l_x_L+l_x_R)/2;
    l_y_D = 0.15; l_y_U = 0.95; l_y_M = (l_y_D+l_y_U)/2; depth_y = items*depth_i;
    if pos_x == "L":
        l_x_min = l_x_L
        l_x_max = l_x_L+width_x
    elif pos_x == "C":
        l_x_min = l_x_C-width_x/2
        l_x_max = l_x_C+width_x/2
    elif pos_x == "R":
        l_x_min = l_x_R-width_x
        l_x_max = l_x_R
    if pos_y == "D":
        l_y_min = l_y_D
        l_y_max = l_y_D+depth_y
    elif pos_y == "M":
        l_y_min = l_y_M-depth_y/2
        l_y_max = l_y_M+depth_y/2
    elif pos_y == "U":
        l_y_min = l_y_U-depth_y
        l_y_max = l_y_U

# X_label 
# Canvas Plot Range
# X_min X_max
def hist_print(hist, t, x_label, x_div, x_min, x_max):
    canvas = ROOT.TCanvas("c")
    canvas.cd()
    hist.Draw()
    hist.SetLineColor( color[1] )
    hist.SetLineWidth(2)
    hist.SetTitle(";"+x_label+"; Events")
    hist.GetYaxis().SetTitleOffset(1.15)
    #hist.SetMinimum(0.9*min(hist.GetMinimum(),hist.GetMinimum()))
    hist.SetMinimum(0.1)
    hist.SetMaximum(1.1*max(hist.GetMaximum(),hist.GetMaximum()))
    hist.SetAxisRange(x_min,x_max, "X")
    hist.SetNdivisions(x_div)

    posleg("R","M",2)

    legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
    legend.SetTextSize(0.035)
    legend.SetBorderSize(1)
    legend.SetHeader("#kappa_{#lambda}="+str(kL[0]),"C")
    legend.AddEntry(hist, taus[t]+" ("+str(int(hist.GetEntries()))+")")
    legend.Draw("same")
    canvas.Update()
    canvas.Print(taus[t]+str(kL[0])+hist.GetName()+".png")
    canvas.Close()
    return hist

def hist_print_compare_deltaR(hists_onhltn, diffhlt):
    diffsub = ["_{1}", "_{2}"]
    diffpng = ["1", "2"]
    canvas = ROOT.TCanvas("c")
    canvas.cd()
    canvas.SetLogy()
    for h in range(len(hists_onhltn)):
        hists_onhltn[h].Draw("same")
        hists_onhltn[h].SetLineColor( color[h])
        hists_onhltn[h].SetLineWidth(3)
        hists_onhltn[h].SetTitle(";#Delta R; Number of online events")
        hists_onhltn[h].GetYaxis().SetTitleOffset(1.05)
        hists_onhltn[h].SetMinimum(0.1)
        posleg("R","U",4)

    legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
    legend.SetTextSize(0.035)
    legend.SetBorderSize(1)
    legend.SetHeader("#kappa_{#lambda}="+str(kL[0]),"C")
    legend.AddEntry(hists_onhltn[0],"Tau "+diffhlt[0]+" ("+str(int(hists_onhltn[0].GetEntries()))+")")
    legend.AddEntry(hists_onhltn[1],"Tau "+diffhlt[1]+" ("+str(int(hists_onhltn[1].GetEntries()))+")")
    legend.Draw("same")
    canvas.Update()

    canvas.Print(taus[0]+str(kL[0])+"on"+diffhlt[0]+".png")
    canvas.Close()

list_order = [
        "p_{T}^{#tau}",
        "p_{T}^{#tau} leading",
        "p_{T}^{#tau} Subleading",
        "RNN Score",
        "Prong"
        ]

#list_range =[
#        []
#        ]

def hist_print_compare(hists_onhltn, diffhlt, x_label, t):
    canvas = ROOT.TCanvas("c")
    canvas.cd()
    canvas.SetLogy()
    for h in range(len(hists_onhltn)):
        hists_onhltn[h].Draw("same")
        hists_onhltn[h].SetLineColor( color[h])
        hists_onhltn[h].SetLineWidth(2)
        hists_onhltn[h].SetTitle(";"+x_label+"; Number of online events")
        hists_onhltn[h].GetYaxis().SetTitleOffset(1.05)
        hists_onhltn[h].SetMinimum(0.1)
    posleg("R","U",4)
    legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
    legend.SetTextSize(0.035)
    legend.SetBorderSize(1)
    legend.SetHeader(x_label+"#kappa_{#lambda}="+str(kL[0]),"C")
    for h in range(len(hists_onhltn)):
        legend.AddEntry(hists_onhltn[h],"Tau "+diffhlt[h]+" ("+str(int(hists_onhltn[h].GetEntries()))+")")
    legend.Draw("same")
    canvas.Update()
    canvas.Print(taus[t]+"_"+x_label+".png")
    canvas.Close()

# loop over the root file and get deltaR
# comparing leading and subleading values
def tree_loop_deltaR( input_root, t):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open( input_root ,"READ")

    tree = inFile.Get("analysis")
    entries = range(tree.GetEntries())

    hist_onhltptdeltaR = ROOT.TH1D("onhltptdeltaR", "",50, -1, 4)
    hist_onhltptdeltaR_lead = ROOT.TH1D("onhltptdeltaR_lead", "",50, -1, 4)
    hist_onhltptdeltaR_sublead = ROOT.TH1D("onhltptdeltaR_sublead", "",50, -1, 4)

    hist_onhltetadeltaR = ROOT.TH1D("onhltetadeltaR", "",50, -1, 4)
    hist_onhltetadeltaR_lead = ROOT.TH1D("onhltetadeltaR_lead", "",50, -1, 4)
    hist_onhltetadeltaR_sublead = ROOT.TH1D("onhltetadeltaR_sublead", "",50, -1, 4)
    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT_1 = getattr(tree, "HLT_ETA25_r22")

        cond_pt = True
        cond_eta = True

        k_on = len(tree.Offline_Matched_Taus)

        if cond_pt:
            for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                vec= tree.TrigMatched_Taus_HLTptfl[i].Vect()
                for j in range(k_on):
                    hist_onhltptdeltaR.Fill(tree.Offline_Matched_Taus[j].Vect().DeltaR(vec))
                    if(i==0): 
                        hist_onhltptdeltaR_lead.Fill(tree.Offline_Matched_Taus[j].Vect().DeltaR(vec))
                    if(i==1): 
                        hist_onhltptdeltaR_sublead.Fill(tree.Offline_Matched_Taus[j].Vect().DeltaR(vec))

        if cond_eta:
            for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                vec= tree.TrigMatched_Taus_HLTetafl[i].Vect()
                for j in range(k_on):
                    hist_onhltetadeltaR.Fill(tree.Offline_Matched_Taus[j].Vect().DeltaR(vec))
                    if(i==0): 
                        hist_onhltetadeltaR_lead.Fill(tree.Offline_Matched_Taus[j].Vect().DeltaR(vec))
                    if(i==1): 
                        hist_onhltetadeltaR_sublead.Fill(tree.Offline_Matched_Taus[j].Vect().DeltaR(vec))

    diffhlt = ["both","lead", "sublead"]
    hists_onhltn = [ hist_onhltptdeltaR, hist_onhltptdeltaR_lead,hist_onhltptdeltaR_sublead]
    hist_print_compare(hists_onhltn, diffhlt, "pt #Delta R", t)

    diffhlt = ["both","lead", "sublead"]
    hists_onhltn = [ hist_onhltetadeltaR, hist_onhltetadeltaR_lead,hist_onhltetadeltaR_sublead]
    hist_print_compare(hists_onhltn, diffhlt, "eta #Delta R", t)

# Loop over the root file interested in
# for hltpt 
def tree_loop_hltpt( input_root, t ):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open( input_root ,"READ")

    print("Start Looping ", taus[t])
    tree = inFile.Get("analysis")
    entries = range(tree.GetEntries())
    hltoff = []
    hltpt = []
    hlteta = []

####Off_Matched_Tau##################################################################################
    hist_offhltpt = ROOT.TH1D("offhltpt","",200,0,1000)
    hist_offhltpt_lead = ROOT.TH1D("offhltpt_lead","",200,0,1000)
    hist_offhltpt_sublead = ROOT.TH1D("offhltpt_sublead","",200,0,1000)
    hist_offhltrnn = ROOT.TH1D("offhlt_rnn","",100,0,1)
    hist_offhltprong = ROOT.TH1D("offhlt_prong","",25,0,25)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT_1 = getattr(tree, "HLT_ETA25_r22")

        cond_pt = True
        cond_eta = True
        if cond_pt:
            for i in range(len(tree.Offline_Matched_Taus)):
                hist_offhltpt.Fill(tree.Offline_Matched_Taus[i].Pt(),1)
                if(i==0): hist_offhltpt_lead.Fill(tree.Offline_Matched_Taus[0].Pt(),1)
                if(i==1): hist_offhltpt_sublead.Fill(tree.Offline_Matched_Taus[1].Pt(),1)
            for j in range(len(tree.Off_Matched_TauRNN)):
                hist_offhltrnn.Fill(tree.Off_Matched_TauRNN[j],1)
            for k in range(len(tree.Off_Matched_TauProng)):
                hist_offhltprong.Fill(tree.Off_Matched_TauProng[k], 1)

    hltoff.append(hist_offhltpt)
    hltoff.append(hist_offhltpt_lead)
    hltoff.append(hist_offhltpt_sublead)
    hltoff.append(hist_offhltrnn)
    hltoff.append(hist_offhltprong)
######################################################################################

####TrigMatched_Taus_HLTptfl##################################################################################
    hist_onhltptpt = ROOT.TH1D("onhltptpt","",200,0,1000)
    hist_onhltptpt_lead = ROOT.TH1D("onhltptpt_lead","",200,0,1000)
    hist_onhltptpt_sublead = ROOT.TH1D("onhltptpt_sublead","",200,0,1000)
    hist_onhltptrnn = ROOT.TH1D("onhltpt_rnn","",100,0,1)
    hist_onhltptprong = ROOT.TH1D("onhltpt_prong","",25,0,25)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT_1 = getattr(tree, "HLT_ETA25_r22")

        cond_pt = True
        cond_eta = True
        if cond_pt:
            for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                hist_onhltptpt.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                if(i==0): hist_onhltptpt_lead.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                if(i==1): hist_onhltptpt_sublead.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
            for j in range(len(tree.TrigMatched_rnn_HLTptfl)):
                hist_onhltptrnn.Fill(tree.TrigMatched_rnn_HLTptfl[j],1)
            for k in range(len(tree.TrigMatched_rnn_HLTptfl)):
                hist_onhltptprong.Fill(tree.TrigMatched_prong_HLTptfl[k], 1)
    hltpt.append(hist_onhltptpt)
    hltpt.append(hist_onhltptpt_lead)
    hltpt.append(hist_onhltptpt_sublead)
    hltpt.append(hist_onhltptrnn)
    hltpt.append(hist_onhltptprong)
######################################################################################

####TrigMatched_Taus_HLTetafl##################################################################################
    hist_onhltetapt = ROOT.TH1D("onhltetapt","",200,0,1000)
    hist_onhltetapt_lead = ROOT.TH1D("onhltetapt_lead","",200,0,1000)
    hist_onhltetapt_sublead = ROOT.TH1D("onhltetapt_sublead","",200,0,1000)
    hist_onhltetarnn = ROOT.TH1D("onhlteta_rnn","",100,0,1)
    hist_onhltetaprong = ROOT.TH1D("onhlteta_prong","",25,0,25)

    # Loop over entries
    for entry in entries:
        tree.GetEntry(entry)
        if taus[t] == "r22_Pass":
            HLT_1 = getattr(tree, "HLT_J25_r22")
            HLT_1 = getattr(tree, "HLT_ETA25_r22")

        cond_pt = True
        cond_eta = True
        if cond_eta:
            for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                hist_onhltetapt.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                if(i==0): hist_onhltetapt_lead.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                if(i==1): hist_onhltetapt_sublead.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
            for j in range(len(tree.TrigMatched_rnn_HLTetafl)):
                hist_onhltetarnn.Fill(tree.TrigMatched_rnn_HLTetafl[j],1)
            for k in range(len(tree.TrigMatched_rnn_HLTetafl)):
                hist_onhltetaprong.Fill(tree.TrigMatched_prong_HLTetafl[k], 1)

    hlteta.append(hist_onhltetapt)
    hlteta.append(hist_onhltetapt_lead)
    hlteta.append(hist_onhltetapt_sublead)
    hlteta.append(hist_onhltetarnn)
    hlteta.append(hist_onhltetaprong)
######################################################################################



    for i in range(5):
        hist_print_compare([hltoff[i],hltpt[i], hlteta[i]], 
                ["off", "pt", "eta"], 
                list_order[i], t)
    #return hl
    # Plots
    #hl.append(hist_print(hist_onhltptpt, t, "p^{#tau}_{T}",20, 0, 100))
    #hl.append(hist_print(hist_onhltptpt_lead, t, "p_{T}^{#tau}",20, 0, 100))
    #hl.append(hist_print(hist_onhltptpt_sublead, t, "p^{#tau}_{T}", 20, 0, 100))
    #hl.append(hist_print(hist_onhltptrnn, t, "RNN Score", 20 ,0, 1))
    #hl.append(hist_print(hist_onhltptprong, t, "Prong",10, 0, 10 ))
    #hl.append(hist_print(hist_onhltetapt, t, "p^{#tau}_{T}",20, 0, 100))
    #hl.append(hist_print(hist_onhltetapt_lead, t, "p_{T}^{#tau}",20, 0, 100))
    #hl.append(hist_print(hist_onhltetapt_sublead, t, "p^{#tau}_{T}", 20, 0, 100))
    #hl.append(hist_print(hist_onhltetarnn, t, "RNN Score", 20 ,0, 1))
    #hl.append(hist_print(hist_onhltetaprong, t, "Prong",10, 0, 10 ))


def main():
    #tree_loop_deltaR("r22_Pass.root", 0)
    #tree_loop_hltpt("r22_Pass.root", 0)
    #hlteta = tree_loop_hlteta("r22_Pass.root", 0)
    #tree_loop_deltaR("r22_PassFail.root", 1)
    #tree_loop_hltpt("r22_PassFail.root", 1)
    #tree_loop_deltaR("Tau0_Pass.root", 2)
    #tree_loop_hltpt("Tau0_Pass.root", 2)
    tree_loop_deltaR("Tau0_PassFail.root", 3)
    tree_loop_hltpt("Tau0_PassFail.root", 3)


if __name__ == "__main__" :
    print("Hello, Start Ploting for HLT")
    main()

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
taus = ["passfail"]
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

for t in range(len(taus)):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open("r22_Pass.root","READ")
        if kL[k] == 10:
            inFile = ROOT.TFile.Open("r22_PassedFailed.root","READ")

        tree = inFile.Get("analysis")

        hist_prev_L1_1 = ROOT.TH1D("prev_L1_1","",2,0,2)
        hist_prev_L1_2 = ROOT.TH1D("prev_L1_2","",2,0,2)
        hist_prev_HLT_1 = ROOT.TH1D("prev_HLT_1","",2,0,2)
        hist_prev_HLT_2 = ROOT.TH1D("prev_HLT_2","",2,0,2)

        hist_prev_onhltptn = ROOT.TH1D("prev_onhltptn","",10,0,10)
        hist_prev_onhltptn_L1_1 = ROOT.TH1D("prev_onhltptn_L1_1","",10,0,10)
        hist_prev_onhltptn_HLT_1 = ROOT.TH1D("prev_onhltptnd_HLT_1","",10,0,10)
        hist_prev_onhltetan = ROOT.TH1D("prev_onhltetan","",10,0,10)
        hist_prev_onhltetan_L1_2 = ROOT.TH1D("prev_onhltetan_L1_2","",10,0,10)
        hist_prev_onhltetan_HLT_2 = ROOT.TH1D("prev_onhltetan_HLT_2","",10,0,10)

        hist_L1_1 = ROOT.TH1D("L1_1","",2,0,2)
        hist_L1_2 = ROOT.TH1D("L1_2","",2,0,2)
        hist_HLT_1 = ROOT.TH1D("HLT_1","",2,0,2)
        hist_HLT_2 = ROOT.TH1D("HLT_2","",2,0,2)

        hist_onhltptn = ROOT.TH1D("onhltptn","",10,0,10)
        hist_onhltptn_L1_1 = ROOT.TH1D("onhltptn_L1_1","",10,0,10)
        hist_onhltptn_HLT_1 = ROOT.TH1D("onhltptnd_HLT_1","",10,0,10)
        hist_onhltetan = ROOT.TH1D("onhltetan","",10,0,10)
        hist_onhltetan_L1_2 = ROOT.TH1D("onhltetan_L1_2","",10,0,10)
        hist_onhltetan_HLT_2 = ROOT.TH1D("onhltetan_HLT_2","",10,0,10)

        hist_onhltptpt = ROOT.TH1D("onhltptpt","",200,0,1000)
        hist_onhltpt0pt = ROOT.TH1D("onhltpt0pt","",200,0,1000)
        hist_onhltpt1pt = ROOT.TH1D("onhltpt1pt","",200,0,1000)
        hist_onhltptpt_L1_1 = ROOT.TH1D("onhltptpt_L1_1","",200,0,1000)
        hist_onhltpt0pt_L1_1 = ROOT.TH1D("onhltpt0pt_L1_1","",200,0,1000)
        hist_onhltpt1pt_L1_1 = ROOT.TH1D("onhltpt1pt_L1_1","",200,0,1000)
        hist_onhltptpt_HLT_1 = ROOT.TH1D("onhltptpt_HLT_1","",200,0,1000)
        hist_onhltpt0pt_HLT_1 = ROOT.TH1D("onhltpt0pt_HLT_1","",200,0,1000)
        hist_onhltpt1pt_HLT_1 = ROOT.TH1D("onhltpt1pt_HLT_1","",200,0,1000)

        hist_onhltetapt = ROOT.TH1D("onhltetapt","",200,0,1000)
        hist_onhlteta0pt = ROOT.TH1D("onhlteta0pt","",200,0,1000)
        hist_onhlteta1pt = ROOT.TH1D("onhlteta1pt","",200,0,1000)
        hist_onhltetapt_L1_2 = ROOT.TH1D("onhltetapt_L1_2","",200,0,1000)
        hist_onhlteta0pt_L1_2 = ROOT.TH1D("onhlteta0pt_L1_2","",200,0,1000)
        hist_onhlteta1pt_L1_2 = ROOT.TH1D("onhlteta1pt_L1_2","",200,0,1000)
        hist_onhltetapt_HLT_2 = ROOT.TH1D("onhltetapt_HLT_2","",200,0,1000)
        hist_onhlteta0pt_HLT_2 = ROOT.TH1D("onhlteta0pt_HLT_2","",200,0,1000)
        hist_onhlteta1pt_HLT_2 = ROOT.TH1D("onhlteta1pt_HLT_2","",200,0,1000)

        hist_onhltptpt_z = ROOT.TH1D("onhltptpt_z","",50,0,50)
        hist_onhltpt0pt_z = ROOT.TH1D("onhltpt0pt_z","",50,0,50)
        hist_onhltpt1pt_z = ROOT.TH1D("onhltpt1pt_z","",50,0,50)
        hist_onhltptpt_L1_1_z = ROOT.TH1D("onhltptpt_L1_1_z","",50,0,50)
        hist_onhltpt0pt_L1_1_z = ROOT.TH1D("onhltpt0pt_L1_1_z","",50,0,50)
        hist_onhltpt1pt_L1_1_z = ROOT.TH1D("onhltpt1pt_L1_1_z","",50,0,50)
        hist_onhltptpt_HLT_1_z = ROOT.TH1D("onhltptpt_HLT_1_z","",50,0,50)
        hist_onhltpt0pt_HLT_1_z = ROOT.TH1D("onhltpt0pt_HLT_1_z","",50,0,50)
        hist_onhltpt1pt_HLT_1_z = ROOT.TH1D("onhltpt1pt_HLT_1_z","",50,0,50)

        hist_onhltetapt_z = ROOT.TH1D("onhltetapt_z","",50,0,50)
        hist_onhlteta0pt_z = ROOT.TH1D("onhlteta0pt_z","",50,0,50)
        hist_onhlteta1pt_z = ROOT.TH1D("onhlteta1pt_z","",50,0,50)
        hist_onhltetapt_L1_2_z = ROOT.TH1D("onhltetapt_L1_2_z","",50,0,50)
        hist_onhlteta0pt_L1_2_z = ROOT.TH1D("onhlteta0pt_L1_2_z","",50,0,50)
        hist_onhlteta1pt_L1_2_z = ROOT.TH1D("onhlteta1pt_L1_2_z","",50,0,50)
        hist_onhltetapt_HLT_2_z = ROOT.TH1D("onhltetapt_HLT_2_z","",50,0,50)
        hist_onhlteta0pt_HLT_2_z = ROOT.TH1D("onhlteta0pt_HLT_2_z","",50,0,50)
        hist_onhlteta1pt_HLT_2_z = ROOT.TH1D("onhlteta1pt_HLT_2_z","",50,0,50)

        hist_onhltptMhpt_z = ROOT.TH1D("onhltptMhpt_z","",50,0,50)
        hist_onhltptMhpt_L1_1_z = ROOT.TH1D("onhltptMhpt_L1_1_z","",50,0,50)
        hist_onhltptMhpt_HLT_1_z = ROOT.TH1D("onhltptMhpt_HLT_1_z","",50,0,50)
        hist_onhltetaMhpt_z = ROOT.TH1D("onhltetaMhpt_z","",50,0,50)
        hist_onhltetaMhpt_L1_2_z = ROOT.TH1D("onhltetaMhpt_L1_2_z","",50,0,50)
        hist_onhltetaMhpt_HLT_2_z = ROOT.TH1D("onhltetaMhpt_HLT_2_z","",50,0,50)

        keep_cut_L1_1 = -100
        keep_cut_L1_2 = -100
        keep_cut_HLT_1 = -100
        keep_cut_HLT_2 = -100
        keep_n_pt = -100
        keep_n_eta = -100

        entries = range(tree.GetEntries())
        for entry in entries:
            if entry % printer == 0: print("Entry: %s/%s." % (entry, len(entries)-1))
            tree.GetEntry(entry)

            L1_1 = getattr(tree, "L1_J25")
            L1_2 = getattr(tree, "L1_ETA25")
            if taus[t] == "passfail":
                HLT_1 = getattr(tree, "HLT_J25_Tau0")
                HLT_2 = getattr(tree, "HLT_ETA25_Tau0")
            if taus[t] == "pass":
                HLT_1 = getattr(tree, "HLT_J25_r22")
                HLT_2 = getattr(tree, "HLT_ETA25_r22")

            cut_L1_1 = L1_1; cut_L1_2 = L1_2; cut_HLT_1 = HLT_1; cut_HLT_2 = HLT_2

            hist_L1_1.Fill(int(cut_L1_1),1)
            hist_L1_2.Fill(int(cut_L1_2),1)
            hist_HLT_1.Fill(int(cut_HLT_1),1)
            hist_HLT_2.Fill(int(cut_HLT_2),1)

            cond_pt = True
            #cond_pt = len(tree.TrigMatched_Taus_HLTptfl) < 2
            #cond_pt = len(tree.TrigMatched_Taus_HLTptfl) >= 2
            cond_eta = True
            #cond_eta = len(tree.TrigMatched_Taus_HLTetafl) < 2
            #cond_eta = len(tree.TrigMatched_Taus_HLTetafl) >= 2

            ptMh = 0; i_ptMh = -1;
            if cond_pt:
                for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltptpt_z.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (ptMh == 0) and tree.TrigMatched_TauIDm_HLTptfl[i]:
                        ptMh = 1;
                        i_ptMh = i;
                    if (i == 0):
                        hist_onhltpt0pt.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                        hist_onhltpt0pt_z.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1):
                        hist_onhltpt1pt.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                        hist_onhltpt1pt_z.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                hist_onhltptn.Fill(len(tree.TrigMatched_Taus_HLTptfl))
                if ptMh: hist_onhltptMhpt_z.Fill(tree.TrigMatched_Taus_HLTptfl[i_ptMh].Pt(),1)

                if cut_L1_1:
                    for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                        hist_onhltptpt_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                        hist_onhltptpt_L1_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                        if (i == 0):
                            hist_onhltpt0pt_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                            hist_onhltpt0pt_L1_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                        if (i == 1):
                            hist_onhltpt1pt_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                            hist_onhltpt1pt_L1_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                    hist_onhltptn_L1_1.Fill(len(tree.TrigMatched_Taus_HLTptfl))
                    if ptMh: hist_onhltptMhpt_L1_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[i_ptMh].Pt(),1)

                if cut_HLT_1:
                    for i in range(len(tree.TrigMatched_Taus_HLTptfl)):
                        hist_onhltptpt_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                        hist_onhltptpt_HLT_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                        if (i == 0):
                            hist_onhltpt0pt_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                            hist_onhltpt0pt_HLT_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                        if (i == 1):
                            hist_onhltpt1pt_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                            hist_onhltpt1pt_HLT_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                    hist_onhltptn_HLT_1.Fill(len(tree.TrigMatched_Taus_HLTptfl))
                    if ptMh: hist_onhltptMhpt_HLT_1_z.Fill(tree.TrigMatched_Taus_HLTptfl[i_ptMh].Pt(),1)

            etaMh = 0; i_etaMh = -1;
            if cond_eta:
                for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetapt_z.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (etaMh == 0) and tree.TrigMatched_TauIDm_HLTetafl[i]:
                        etaMh = 1;
                        i_etaMh = i;
                    if (i == 0):
                        hist_onhlteta0pt.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                        hist_onhlteta0pt_z.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1):
                        hist_onhlteta1pt.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                        hist_onhlteta1pt_z.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                hist_onhltetan.Fill(len(tree.TrigMatched_Taus_HLTetafl))
                if etaMh: hist_onhltetaMhpt_z.Fill(tree.TrigMatched_Taus_HLTetafl[i_etaMh].Pt(),1)

                if cut_L1_2:
                    for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                        hist_onhltetapt_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                        hist_onhltetapt_L1_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                        if (i == 0):
                            hist_onhlteta0pt_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                            hist_onhlteta0pt_L1_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                        if (i == 1):
                            hist_onhlteta1pt_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                            hist_onhlteta1pt_L1_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                    hist_onhltetan_L1_2.Fill(len(tree.TrigMatched_Taus_HLTetafl))
                    if etaMh: hist_onhltetaMhpt_L1_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[i_etaMh].Pt(),1)

                if cut_HLT_2:
                    for i in range(len(tree.TrigMatched_Taus_HLTetafl)):
                        hist_onhltetapt_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                        hist_onhltetapt_HLT_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                        if (i == 0):
                            hist_onhlteta0pt_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                            hist_onhlteta0pt_HLT_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                        if (i == 1):
                            hist_onhlteta1pt_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                            hist_onhlteta1pt_HLT_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                    hist_onhltetan_HLT_2.Fill(len(tree.TrigMatched_Taus_HLTetafl))
                    if etaMh: hist_onhltetaMhpt_HLT_2_z.Fill(tree.TrigMatched_Taus_HLTetafl[i_etaMh].Pt(),1)

            if (len(tree.TrigMatched_Taus_HLTptfl) == 0) or (len(tree.TrigMatched_Taus_HLTptfl) == 1):
                hist_prev_L1_1.Fill(int(keep_cut_L1_1),1)
                hist_prev_HLT_1.Fill(int(keep_cut_HLT_1),1)
                hist_prev_onhltptn.Fill(keep_n_pt)
                if cut_L1_1:
                    hist_prev_onhltptn_L1_1.Fill(keep_n_pt)
                if cut_HLT_1:
                    hist_prev_onhltptn_HLT_1.Fill(keep_n_pt)

            if (len(tree.TrigMatched_Taus_HLTetafl) == 0) or (len(tree.TrigMatched_Taus_HLTetafl) == 1):
                hist_prev_L1_2.Fill(int(keep_cut_L1_2),1)
                hist_prev_HLT_2.Fill(int(keep_cut_HLT_2),1)
                hist_prev_onhltetan.Fill(keep_n_eta)
                if cut_L1_2:
                    hist_prev_onhltetan_L1_2.Fill(keep_n_eta)
                if cut_HLT_2:
                    hist_prev_onhltetan_HLT_2.Fill(keep_n_eta)

            keep_cut_L1_1 = int(cut_L1_1)
            keep_cut_L1_2 = int(cut_L1_2)
            keep_cut_HLT_1 = int(cut_HLT_1)
            keep_cut_HLT_2 = int(cut_HLT_2)
            keep_n_pt = len(tree.TrigMatched_Taus_HLTptfl)
            keep_n_eta = len(tree.TrigMatched_Taus_HLTetafl)

        hists_prev_L1 = [hist_prev_L1_1, hist_prev_L1_2]
        hists_prev_HLT = [hist_prev_HLT_1, hist_prev_HLT_2]
        diffsub = ["_{1}", "_{2}"]
        diffpng = ["1", "2"]
        for h in range(len(hists_prev_L1)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            hists_prev_L1[h].Draw()
            hists_prev_L1[h].SetLineColor(ROOT.kBlue)
            hists_prev_L1[h].SetLineWidth(2)
            hists_prev_HLT[h].Draw("SAME")
            hists_prev_HLT[h].SetLineColor(ROOT.kRed)
            hists_prev_HLT[h].SetLineWidth(1)
            hists_prev_L1[h].SetTitle(";Trigger value; n#circ online events (previous to 0 or 1 #tau event)")
            hists_prev_L1[h].GetYaxis().SetTitleOffset(1.15)
            hists_prev_L1[h].SetMinimum(0.9*min(hists_prev_L1[h].GetMinimum(),hists_prev_HLT[h].GetMinimum()))
            hists_prev_L1[h].SetMaximum(1.1*max(hists_prev_L1[h].GetMaximum(),hists_prev_HLT[h].GetMaximum()))
            hists_prev_L1[h].SetNdivisions(2)
            posleg("R","M",3)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_prev_L1[h],"Pass L1"+diffsub[h]+" ("+str(int(hists_prev_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_prev_HLT[h],"Pass HLT"+diffsub[h]+" ("+str(int(hists_prev_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"trg"+diffpng[h]+"prev.png")
            canvas.Close()

        hists_prev_onhltn = [hist_prev_onhltptn, hist_prev_onhltetan]
        hists_prev_onhltn_L1 = [hist_prev_onhltptn_L1_1, hist_prev_onhltetan_L1_2]
        hists_prev_onhltn_HLT = [hist_prev_onhltptn_HLT_1, hist_prev_onhltetan_HLT_2]
        diffhlt = ["hltpt", "hlteta"]
        diffsub = ["_{1}", "_{2}"]
        diffpng = ["1", "2"]
        for h in range(len(hists_prev_onhltn)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_prev_onhltn[h].Draw()
            hists_prev_onhltn[h].SetLineColor(ROOT.kBlack)
            hists_prev_onhltn[h].SetLineWidth(3)
            hists_prev_onhltn_L1[h].Draw("same")
            hists_prev_onhltn_L1[h].SetLineColor(ROOT.kBlue)
            hists_prev_onhltn_L1[h].SetLineWidth(2)
            hists_prev_onhltn_HLT[h].Draw("same")
            hists_prev_onhltn_HLT[h].SetLineColor(ROOT.kRed)
            hists_prev_onhltn_HLT[h].SetLineWidth(1)
            hists_prev_onhltn[h].SetTitle(";n#circ #tau;n#circ online events (previous to 0 or 1 #tau event)")
            hists_prev_onhltn[h].GetYaxis().SetTitleOffset(1.05)
            hists_prev_onhltn[h].SetMinimum(0.1)
            posleg("R","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_prev_onhltn[h],"Tau "+diffhlt[h]+" ("+str(int(hists_prev_onhltn[h].GetEntries()))+")")
            legend.AddEntry(hists_prev_onhltn_L1[h],"Pass L1"+diffsub[h]+" ("+str(int(hists_prev_onhltn_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_prev_onhltn_HLT[h],"Pass HLT"+diffsub[h]+" ("+str(int(hists_prev_onhltn_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diffhlt[h]+"ntrg"+diffpng[h]+"prev.png")
            canvas.Close()

        hists_L1 = [hist_L1_1, hist_L1_2]
        hists_HLT = [hist_HLT_1, hist_HLT_2]
        diffsub = ["_{1}", "_{2}"]
        diffpng = ["1", "2"]
        for h in range(len(hists_L1)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            hists_L1[h].Draw()
            hists_L1[h].SetLineColor(ROOT.kBlue)
            hists_L1[h].SetLineWidth(2)
            hists_HLT[h].Draw("SAME")
            hists_HLT[h].SetLineColor(ROOT.kRed)
            hists_HLT[h].SetLineWidth(1)
            hists_L1[h].SetTitle(";Trigger value; n#circ online events (previous to 0 or 1 #tau event)")
            hists_L1[h].GetYaxis().SetTitleOffset(1.05)
            hists_L1[h].SetMinimum(0.9*min(hists_L1[h].GetMinimum(),hists_HLT[h].GetMinimum()))
            hists_L1[h].SetMaximum(1.1*max(hists_L1[h].GetMaximum(),hists_HLT[h].GetMaximum()))
            hists_L1[h].SetNdivisions(2)
            posleg("R","M",3)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_L1[h],"Pass L1"+diffsub[h]+" ("+str(int(hists_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_HLT[h],"Pass HLT"+diffsub[h]+" ("+str(int(hists_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"trg"+diffpng[h]+".png")
            canvas.Close()

        hists_onhltn = [hist_onhltptn, hist_onhltetan]
        hists_onhltn_L1 = [hist_onhltptn_L1_1, hist_onhltetan_L1_2]
        hists_onhltn_HLT = [hist_onhltptn_HLT_1, hist_onhltetan_HLT_2]
        diffhlt = ["hltpt", "hlteta"]
        diffsub = ["_{1}", "_{2}"]
        diffpng = ["1", "2"]
        for h in range(len(hists_onhltn)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltn[h].Draw()
            hists_onhltn[h].SetLineColor(ROOT.kBlack)
            hists_onhltn[h].SetLineWidth(3)
            hists_onhltn_L1[h].Draw("same")
            hists_onhltn_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltn_L1[h].SetLineWidth(2)
            hists_onhltn_HLT[h].Draw("same")
            hists_onhltn_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltn_HLT[h].SetLineWidth(1)
            hists_onhltn[h].SetTitle(";n#circ #tau;n#circ online events")
            hists_onhltn[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltn[h].SetMinimum(0.1)
            posleg("R","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltn[h],"Tau "+diffhlt[h]+" ("+str(int(hists_onhltn[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltn_L1[h],"Pass L1"+diffsub[h]+" ("+str(int(hists_onhltn_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltn_HLT[h],"Pass HLT"+diffsub[h]+" ("+str(int(hists_onhltn_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diffhlt[h]+"ntrg"+diffpng[h]+".png")
            canvas.Close()

        hists_onhltptpt = [hist_onhltptpt, hist_onhltpt0pt, hist_onhltpt1pt]
        hists_onhltptpt_L1_1 = [hist_onhltptpt_L1_1, hist_onhltpt0pt_L1_1, hist_onhltpt1pt_L1_1]
        hists_onhltptpt_HLT_1 = [hist_onhltptpt_HLT_1, hist_onhltpt0pt_HLT_1, hist_onhltpt1pt_HLT_1]
        difftau = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltptpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltptpt[h].Draw()
            hists_onhltptpt[h].SetLineColor(ROOT.kBlack)
            hists_onhltptpt[h].SetLineWidth(3)
            hists_onhltptpt_L1_1[h].Draw("same")
            hists_onhltptpt_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltptpt_L1_1[h].SetLineWidth(2)
            hists_onhltptpt_HLT_1[h].Draw("same")
            hists_onhltptpt_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltptpt_HLT_1[h].SetLineWidth(1)
            hists_onhltptpt[h].SetTitle(";p^{#tau}_{T} (GeV);n#circ online "+difftau[h]+" #tau")
            hists_onhltptpt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltptpt[h].SetAxisRange(0,500,"X")
            hists_onhltptpt[h].SetMinimum(0.1)
            posleg("R","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltptpt[h],"Tau hltpt ("+str(int(hists_onhltptpt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltptpt_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltptpt_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhltpt"+diffpng[h]+"pttrg1.png")
            canvas.Close()

        hists_onhltetapt = [hist_onhltetapt, hist_onhlteta0pt, hist_onhlteta1pt]
        hists_onhltetapt_L1_2 = [hist_onhltetapt_L1_2, hist_onhlteta0pt_L1_2, hist_onhlteta1pt_L1_2]
        hists_onhltetapt_HLT_2 = [hist_onhltetapt_HLT_2, hist_onhlteta0pt_HLT_2, hist_onhlteta1pt_HLT_2]
        difftau = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltetapt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltetapt[h].Draw()
            hists_onhltetapt[h].SetLineColor(ROOT.kBlack)
            hists_onhltetapt[h].SetLineWidth(3)
            hists_onhltetapt_L1_2[h].Draw("same")
            hists_onhltetapt_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltetapt_L1_2[h].SetLineWidth(2)
            hists_onhltetapt_HLT_2[h].Draw("same")
            hists_onhltetapt_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltetapt_HLT_2[h].SetLineWidth(1)
            hists_onhltetapt[h].SetTitle(";p^{#tau}_{T} (GeV);n#circ online "+difftau[h]+" #tau")
            hists_onhltetapt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltetapt[h].SetAxisRange(0,500,"X")
            hists_onhltetapt[h].SetMinimum(0.1)
            posleg("R","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltetapt[h],"Tau hlteta ("+str(int(hists_onhltetapt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltetapt_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltetapt_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhlteta"+diffpng[h]+"pttrg2.png")
            canvas.Close()

        hists_onhltptpt_z = [hist_onhltptpt_z, hist_onhltpt0pt_z, hist_onhltpt1pt_z]
        hists_onhltptpt_L1_1_z = [hist_onhltptpt_L1_1_z, hist_onhltpt0pt_L1_1_z, hist_onhltpt1pt_L1_1_z]
        hists_onhltptpt_HLT_1_z = [hist_onhltptpt_HLT_1_z, hist_onhltpt0pt_HLT_1_z, hist_onhltpt1pt_HLT_1_z]
        difftau = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltptpt_z)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltptpt_z[h].Draw()
            hists_onhltptpt_z[h].SetLineColor(ROOT.kBlack)
            hists_onhltptpt_z[h].SetLineWidth(3)
            hists_onhltptpt_L1_1_z[h].Draw("same")
            hists_onhltptpt_L1_1_z[h].SetLineColor(ROOT.kBlue)
            hists_onhltptpt_L1_1_z[h].SetLineWidth(2)
            hists_onhltptpt_HLT_1_z[h].Draw("same")
            hists_onhltptpt_HLT_1_z[h].SetLineColor(ROOT.kRed)
            hists_onhltptpt_HLT_1_z[h].SetLineWidth(1)
            hists_onhltptpt_z[h].SetTitle(";p^{#tau}_{T} (GeV);n#circ online "+difftau[h]+" #tau")
            hists_onhltptpt_z[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltptpt_z[h].SetMinimum(0.1)
            posleg("L","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltptpt_z[h],"Tau hltpt ("+str(int(hists_onhltptpt_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_L1_1_z[h],"Pass L1_{1} ("+str(int(hists_onhltptpt_L1_1_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_HLT_1_z[h],"Pass HLT_{1} ("+str(int(hists_onhltptpt_HLT_1_z[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhltpt"+diffpng[h]+"pttrg1z.png")
            canvas.Close()

        hists_onhltetapt_z = [hist_onhltetapt_z, hist_onhlteta0pt_z, hist_onhlteta1pt_z]
        hists_onhltetapt_L1_2_z = [hist_onhltetapt_L1_2_z, hist_onhlteta0pt_L1_2_z, hist_onhlteta1pt_L1_2_z]
        hists_onhltetapt_HLT_2_z = [hist_onhltetapt_HLT_2_z, hist_onhlteta0pt_HLT_2_z, hist_onhlteta1pt_HLT_2_z]
        difftau = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltetapt_z)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltetapt_z[h].Draw()
            hists_onhltetapt_z[h].SetLineColor(ROOT.kBlack)
            hists_onhltetapt_z[h].SetLineWidth(3)
            hists_onhltetapt_L1_2_z[h].Draw("same")
            hists_onhltetapt_L1_2_z[h].SetLineColor(ROOT.kBlue)
            hists_onhltetapt_L1_2_z[h].SetLineWidth(2)
            hists_onhltetapt_HLT_2_z[h].Draw("same")
            hists_onhltetapt_HLT_2_z[h].SetLineColor(ROOT.kRed)
            hists_onhltetapt_HLT_2_z[h].SetLineWidth(1)
            hists_onhltetapt_z[h].SetTitle(";p^{#tau}_{T} (GeV);n#circ online "+difftau[h]+" #tau")
            hists_onhltetapt_z[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltetapt_z[h].SetMinimum(0.1)
            posleg("L","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltetapt_z[h],"Tau hlteta ("+str(int(hists_onhltetapt_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_L1_2_z[h],"Pass L1_{2} ("+str(int(hists_onhltetapt_L1_2_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_HLT_2_z[h],"Pass HLT_{2} ("+str(int(hists_onhltetapt_HLT_2_z[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhlteta"+diffpng[h]+"pttrg2z.png")
            canvas.Close()

        hists_onhltMhpt_z = [hist_onhltptMhpt_z, hist_onhltetaMhpt_z]
        hists_onhltMhpt_L1_z = [hist_onhltptMhpt_L1_1_z, hist_onhltetaMhpt_L1_2_z]
        hists_onhltMhpt_HLT_z = [hist_onhltptMhpt_HLT_1_z, hist_onhltetaMhpt_HLT_2_z]
        diffhlt = ["hltpt", "hlteta"]
        diffsub = ["_{1}", "_{2}"]
        diffpng = ["1", "2"]
        for h in range(len(hists_onhltMhpt_z)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltMhpt_z[h].Draw()
            hists_onhltMhpt_z[h].SetLineColor(ROOT.kBlack)
            hists_onhltMhpt_z[h].SetLineWidth(3)
            hists_onhltMhpt_L1_z[h].Draw("same")
            hists_onhltMhpt_L1_z[h].SetLineColor(ROOT.kBlue)
            hists_onhltMhpt_L1_z[h].SetLineWidth(2)
            hists_onhltMhpt_HLT_z[h].Draw("same")
            hists_onhltMhpt_HLT_z[h].SetLineColor(ROOT.kRed)
            hists_onhltMhpt_HLT_z[h].SetLineWidth(1)
            hists_onhltMhpt_z[h].SetTitle(";p^{#tau}_{T} (GeV);n#circ online highest p^{#tau}_{T} #tau (RNN medium)")
            hists_onhltMhpt_z[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltMhpt_z[h].SetMinimum(0.1)
            posleg("L","U",4)
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltMhpt_z[h],"Tau "+diffhlt[h]+" M ("+str(int(hists_onhltMhpt_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltMhpt_L1_z[h],"Pass L1"+diffsub[h]+" ("+str(int(hists_onhltMhpt_L1_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltMhpt_HLT_z[h],"Pass HLT"+diffsub[h]+" ("+str(int(hists_onhltMhpt_HLT_z[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diffhlt[h]+"Mhpttrg"+diffpng[h]+"z.png")
            canvas.Close()

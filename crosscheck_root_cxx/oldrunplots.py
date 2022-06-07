#!/usr/bin/env python
#Version 22.04.14.11.00
import math
import ROOT
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
#taus = ["pass"]
kL = [1,10]
kL = [1]

printer = 5000; down = 0.4
l_x_min_L = 0.145; l_x_max_L = 0.42; l_x_min_C = 0.41; l_x_max_C = 0.685; l_x_min_R = 0.675; l_x_max_R = 0.95;
l_y_min_6 = 0.65; l_y_min_4 = 0.75; l_y_min_3 = 0.8; l_y_min_2 = 0.85; l_y_max_U = 0.95

for t in range(len(taus)):
    for k in range(len(kL)):
        if kL[k] == 1:
            inFile = ROOT.TFile.Open("/eos/user/a/amelo/bbtautautriggeranalysis/600023_"+taus[t]+".root","READ")
        if kL[k] == 10:
            inFile = ROOT.TFile.Open("/eos/user/a/amelo/bbtautau/Output/600024.root","READ")

        tree = inFile.Get("analysis")

        hist_L1_1 = ROOT.TH1D("L1_1","",2,0,2)
        hist_L1_2 = ROOT.TH1D("L1_2","",2,0,2)
        hist_L1 = ROOT.TH1D("L1","",2,0,2)
        hist_HLT_1 = ROOT.TH1D("HLT_1","",2,0,2)
        hist_HLT_2 = ROOT.TH1D("HLT_2","",2,0,2)
        hist_HLT = ROOT.TH1D("HLT","",2,0,2)

        hist_onhltptpt = ROOT.TH1D("onhltptpt","",200,0,1000)
        hist_onhltpt0pt = ROOT.TH1D("onhltpt0pt","",200,0,1000)
        hist_onhltpt1pt = ROOT.TH1D("onhltpt1pt","",200,0,1000)
        hist_onhltptpt_L1_1 = ROOT.TH1D("onhltptpt_L1_1","",200,0,1000)
        hist_onhltpt0pt_L1_1 = ROOT.TH1D("onhltpt0pt_L1_1","",200,0,1000)
        hist_onhltpt1pt_L1_1 = ROOT.TH1D("onhltpt1pt_L1_1","",200,0,1000)
        hist_onhltptpt_L1_2 = ROOT.TH1D("onhltptpt_L1_2","",200,0,1000)
        hist_onhltpt0pt_L1_2 = ROOT.TH1D("onhltpt0pt_L1_2","",200,0,1000)
        hist_onhltpt1pt_L1_2 = ROOT.TH1D("onhltpt1pt_L1_2","",200,0,1000)
        hist_onhltptpt_L1 = ROOT.TH1D("onhltptpt_L1","",200,0,1000)
        hist_onhltpt0pt_L1 = ROOT.TH1D("onhltpt0pt_L1","",200,0,1000)
        hist_onhltpt1pt_L1 = ROOT.TH1D("onhltpt1pt_L1","",200,0,1000)
        hist_onhltptpt_HLT_1 = ROOT.TH1D("onhltptpt_HLT_1","",200,0,1000)
        hist_onhltpt0pt_HLT_1 = ROOT.TH1D("onhltpt0pt_HLT_1","",200,0,1000)
        hist_onhltpt1pt_HLT_1 = ROOT.TH1D("onhltpt1pt_HLT_1","",200,0,1000)
        hist_onhltptpt_HLT_2 = ROOT.TH1D("onhltptpt_HLT_2","",200,0,1000)
        hist_onhltpt0pt_HLT_2 = ROOT.TH1D("onhltpt0pt_HLT_2","",200,0,1000)
        hist_onhltpt1pt_HLT_2 = ROOT.TH1D("onhltpt1pt_HLT_2","",200,0,1000)
        hist_onhltptpt_HLT = ROOT.TH1D("onhltptpt_HLT","",200,0,1000)
        hist_onhltpt0pt_HLT = ROOT.TH1D("onhltpt0pt_HLT","",200,0,1000)
        hist_onhltpt1pt_HLT = ROOT.TH1D("onhltpt1pt_HLT","",200,0,1000)

        hist_onhltetapt = ROOT.TH1D("onhltetapt","",200,0,1000)
        hist_onhlteta0pt = ROOT.TH1D("onhlteta0pt","",200,0,1000)
        hist_onhlteta1pt = ROOT.TH1D("onhlteta1pt","",200,0,1000)
        hist_onhltetapt_L1_1 = ROOT.TH1D("onhltetapt_L1_1","",200,0,1000)
        hist_onhlteta0pt_L1_1 = ROOT.TH1D("onhlteta0pt_L1_1","",200,0,1000)
        hist_onhlteta1pt_L1_1 = ROOT.TH1D("onhlteta1pt_L1_1","",200,0,1000)
        hist_onhltetapt_L1_2 = ROOT.TH1D("onhltetapt_L1_2","",200,0,1000)
        hist_onhlteta0pt_L1_2 = ROOT.TH1D("onhlteta0pt_L1_2","",200,0,1000)
        hist_onhlteta1pt_L1_2 = ROOT.TH1D("onhlteta1pt_L1_2","",200,0,1000)
        hist_onhltetapt_L1 = ROOT.TH1D("onhltetapt_L1","",200,0,1000)
        hist_onhlteta0pt_L1 = ROOT.TH1D("onhlteta0pt_L1","",200,0,1000)
        hist_onhlteta1pt_L1 = ROOT.TH1D("onhlteta1pt_L1","",200,0,1000)
        hist_onhltetapt_HLT_1 = ROOT.TH1D("onhltetapt_HLT_1","",200,0,1000)
        hist_onhlteta0pt_HLT_1 = ROOT.TH1D("onhlteta0pt_HLT_1","",200,0,1000)
        hist_onhlteta1pt_HLT_1 = ROOT.TH1D("onhlteta1pt_HLT_1","",200,0,1000)
        hist_onhltetapt_HLT_2 = ROOT.TH1D("onhltetapt_HLT_2","",200,0,1000)
        hist_onhlteta0pt_HLT_2 = ROOT.TH1D("onhlteta0pt_HLT_2","",200,0,1000)
        hist_onhlteta1pt_HLT_2 = ROOT.TH1D("onhlteta1pt_HLT_2","",200,0,1000)
        hist_onhltetapt_HLT = ROOT.TH1D("onhltetapt_HLT","",200,0,1000)
        hist_onhlteta0pt_HLT = ROOT.TH1D("onhlteta0pt_HLT","",200,0,1000)
        hist_onhlteta1pt_HLT = ROOT.TH1D("onhlteta1pt_HLT","",200,0,1000)

        hist_onhltptpt_z = ROOT.TH1D("onhltptpt_z","",50,0,100)
        hist_onhltpt0pt_z = ROOT.TH1D("onhltpt0pt_z","",50,0,100)
        hist_onhltpt1pt_z = ROOT.TH1D("onhltpt1pt_z","",50,0,100)
        hist_onhltptpt_L1_z = ROOT.TH1D("onhltptpt_L1_z","",50,0,100)
        hist_onhltpt0pt_L1_z = ROOT.TH1D("onhltpt0pt_L1_z","",50,0,100)
        hist_onhltpt1pt_L1_z = ROOT.TH1D("onhltpt1pt_L1_z","",50,0,100)
        hist_onhltptpt_HLT_z = ROOT.TH1D("onhltptpt_HLT_z","",50,0,100)
        hist_onhltpt0pt_HLT_z = ROOT.TH1D("onhltpt0pt_HLT_z","",50,0,100)
        hist_onhltpt1pt_HLT_z = ROOT.TH1D("onhltpt1pt_HLT_z","",50,0,100)

        hist_onhltetapt_z = ROOT.TH1D("onhltetapt_z","",50,0,100)
        hist_onhlteta0pt_z = ROOT.TH1D("onhlteta0pt_z","",50,0,100)
        hist_onhlteta1pt_z = ROOT.TH1D("onhlteta1pt_z","",50,0,100)
        hist_onhltetapt_L1_z = ROOT.TH1D("onhltetapt_L1_z","",50,0,100)
        hist_onhlteta0pt_L1_z = ROOT.TH1D("onhlteta0pt_L1_z","",50,0,100)
        hist_onhlteta1pt_L1_z = ROOT.TH1D("onhlteta1pt_L1_z","",50,0,100)
        hist_onhltetapt_HLT_z = ROOT.TH1D("onhltetapt_HLT_z","",50,0,100)
        hist_onhlteta0pt_HLT_z = ROOT.TH1D("onhlteta0pt_HLT_z","",50,0,100)
        hist_onhlteta1pt_HLT_z = ROOT.TH1D("onhlteta1pt_HLT_z","",50,0,100)

        hist_onhltptdR01 = ROOT.TH1D("onhltptdR01","",50,-1,4)
        hist_onhltptdR01_L1_1 = ROOT.TH1D("onhltptdR01_L1_1","",50,-1,4)
        hist_onhltptdR01_L1_2 = ROOT.TH1D("onhltptdR01_L1_2","",50,-1,4)
        hist_onhltptdR01_L1 = ROOT.TH1D("onhltptdR01_L1","",50,-1,4)
        hist_onhltptdR01_HLT_1 = ROOT.TH1D("onhltptdR01_HLT_1","",50,-1,4)
        hist_onhltptdR01_HLT_2 = ROOT.TH1D("onhltptdR01_HLT_2","",50,-1,4)
        hist_onhltptdR01_HLT = ROOT.TH1D("onhltptdR01_HLT","",50,-1,4)
        hist_onhltetadR01 = ROOT.TH1D("onhltetadR01","",50,-1,4)
        hist_onhltetadR01_L1_1 = ROOT.TH1D("onhltetadR01_L1_1","",50,-1,4)
        hist_onhltetadR01_L1_2 = ROOT.TH1D("onhltetadR01_L1_2","",50,-1,4)
        hist_onhltetadR01_L1 = ROOT.TH1D("onhltetadR01_L1","",50,-1,4)
        hist_onhltetadR01_HLT_1 = ROOT.TH1D("onhltetadR01_HLT_1","",50,-1,4)
        hist_onhltetadR01_HLT_2 = ROOT.TH1D("onhltetadR01_HLT_2","",50,-1,4)
        hist_onhltetadR01_HLT = ROOT.TH1D("onhltetadR01_HLT","",50,-1,4)

        hist_onhltptdphi01 = ROOT.TH1D("onhltptdphi01","",50,-1,4)
        hist_onhltptdphi01_L1_1 = ROOT.TH1D("onhltptdphi01_L1_1","",50,-1,4)
        hist_onhltptdphi01_L1_2 = ROOT.TH1D("onhltptdphi01_L1_2","",50,-1,4)
        hist_onhltptdphi01_L1 = ROOT.TH1D("onhltptdphi01_L1","",50,-1,4)
        hist_onhltptdphi01_HLT_1 = ROOT.TH1D("onhltptdphi01_HLT_1","",50,-1,4)
        hist_onhltptdphi01_HLT_2 = ROOT.TH1D("onhltptdphi01_HLT_2","",50,-1,4)
        hist_onhltptdphi01_HLT = ROOT.TH1D("onhltptdphi01_HLT","",50,-1,4)
        hist_onhltetadphi01 = ROOT.TH1D("onhltetadphi01","",50,-1,4)
        hist_onhltetadphi01_L1_1 = ROOT.TH1D("onhltetadphi01_L1_1","",50,-1,4)
        hist_onhltetadphi01_L1_2 = ROOT.TH1D("onhltetadphi01_L1_2","",50,-1,4)
        hist_onhltetadphi01_L1 = ROOT.TH1D("onhltetadphi01_L1","",50,-1,4)
        hist_onhltetadphi01_HLT_1 = ROOT.TH1D("onhltetadphi01_HLT_1","",50,-1,4)
        hist_onhltetadphi01_HLT_2 = ROOT.TH1D("onhltetadphi01_HLT_2","",50,-1,4)
        hist_onhltetadphi01_HLT = ROOT.TH1D("onhltetadphi01_HLT","",50,-1,4)

        hist_onhltptdeta01 = ROOT.TH1D("onhltptdeta01","",50,-1,4)
        hist_onhltptdeta01_L1_1 = ROOT.TH1D("onhltptdeta01_L1_1","",50,-1,4)
        hist_onhltptdeta01_L1_2 = ROOT.TH1D("onhltptdeta01_L1_2","",50,-1,4)
        hist_onhltptdeta01_L1 = ROOT.TH1D("onhltptdeta01_L1","",50,-1,4)
        hist_onhltptdeta01_HLT_1 = ROOT.TH1D("onhltptdeta01_HLT_1","",50,-1,4)
        hist_onhltptdeta01_HLT_2 = ROOT.TH1D("onhltptdeta01_HLT_2","",50,-1,4)
        hist_onhltptdeta01_HLT = ROOT.TH1D("onhltptdeta01_HLT","",50,-1,4)
        hist_onhltetadeta01 = ROOT.TH1D("onhltetadeta01","",50,-1,4)
        hist_onhltetadeta01_L1_1 = ROOT.TH1D("onhltetadeta01_L1_1","",50,-1,4)
        hist_onhltetadeta01_L1_2 = ROOT.TH1D("onhltetadeta01_L1_2","",50,-1,4)
        hist_onhltetadeta01_L1 = ROOT.TH1D("onhltetadeta01_L1","",50,-1,4)
        hist_onhltetadeta01_HLT_1 = ROOT.TH1D("onhltetadeta01_HLT_1","",50,-1,4)
        hist_onhltetadeta01_HLT_2 = ROOT.TH1D("onhltetadeta01_HLT_2","",50,-1,4)
        hist_onhltetadeta01_HLT = ROOT.TH1D("onhltetadeta01_HLT","",50,-1,4)

        hist_onhltptmindR = ROOT.TH1D("onhltptmindR","",50,-1,4)
        hist_onhltptmindR_L1_1 = ROOT.TH1D("onhltptmindR_L1_1","",50,-1,4)
        hist_onhltptmindR_L1_2 = ROOT.TH1D("onhltptmindR_L1_2","",50,-1,4)
        hist_onhltptmindR_L1 = ROOT.TH1D("onhltptmindR_L1","",50,-1,4)
        hist_onhltptmindR_HLT_1 = ROOT.TH1D("onhltptmindR_HLT_1","",50,-1,4)
        hist_onhltptmindR_HLT_2 = ROOT.TH1D("onhltptmindR_HLT_2","",50,-1,4)
        hist_onhltptmindR_HLT = ROOT.TH1D("onhltptmindR_HLT","",50,-1,4)
        hist_onhltetamindR = ROOT.TH1D("onhltetamindR","",50,-1,4)
        hist_onhltetamindR_L1_1 = ROOT.TH1D("onhltetamindR_L1_1","",50,-1,4)
        hist_onhltetamindR_L1_2 = ROOT.TH1D("onhltetamindR_L1_2","",50,-1,4)
        hist_onhltetamindR_L1 = ROOT.TH1D("onhltetamindR_L1","",50,-1,4)
        hist_onhltetamindR_HLT_1 = ROOT.TH1D("onhltetamindR_HLT_1","",50,-1,4)
        hist_onhltetamindR_HLT_2 = ROOT.TH1D("onhltetamindR_HLT_2","",50,-1,4)
        hist_onhltetamindR_HLT = ROOT.TH1D("onhltetamindR_HLT","",50,-1,4)

        hist_onhltptdphimindR = ROOT.TH1D("onhltptdphimindR","",50,-1,4)
        hist_onhltptdphimindR_L1_1 = ROOT.TH1D("onhltptdphimindR_L1_1","",50,-1,4)
        hist_onhltptdphimindR_L1_2 = ROOT.TH1D("onhltptdphimindR_L1_2","",50,-1,4)
        hist_onhltptdphimindR_L1 = ROOT.TH1D("onhltptdphimindR_L1","",50,-1,4)
        hist_onhltptdphimindR_HLT_1 = ROOT.TH1D("onhltptdphimindR_HLT_1","",50,-1,4)
        hist_onhltptdphimindR_HLT_2 = ROOT.TH1D("onhltptdphimindR_HLT_2","",50,-1,4)
        hist_onhltptdphimindR_HLT = ROOT.TH1D("onhltptdphimindR_HLT","",50,-1,4)
        hist_onhltetadphimindR = ROOT.TH1D("onhltetadphimindR","",50,-1,4)
        hist_onhltetadphimindR_L1_1 = ROOT.TH1D("onhltetadphimindR_L1_1","",50,-1,4)
        hist_onhltetadphimindR_L1_2 = ROOT.TH1D("onhltetadphimindR_L1_2","",50,-1,4)
        hist_onhltetadphimindR_L1 = ROOT.TH1D("onhltetadphimindR_L1","",50,-1,4)
        hist_onhltetadphimindR_HLT_1 = ROOT.TH1D("onhltetadphimindR_HLT_1","",50,-1,4)
        hist_onhltetadphimindR_HLT_2 = ROOT.TH1D("onhltetadphimindR_HLT_2","",50,-1,4)
        hist_onhltetadphimindR_HLT = ROOT.TH1D("onhltetadphimindR_HLT","",50,-1,4)

        hist_onhltptdetamindR = ROOT.TH1D("onhltptdetamindR","",50,-1,4)
        hist_onhltptdetamindR_L1_1 = ROOT.TH1D("onhltptdetamindR_L1_1","",50,-1,4)
        hist_onhltptdetamindR_L1_2 = ROOT.TH1D("onhltptdetamindR_L1_2","",50,-1,4)
        hist_onhltptdetamindR_L1 = ROOT.TH1D("onhltptdetamindR_L1","",50,-1,4)
        hist_onhltptdetamindR_HLT_1 = ROOT.TH1D("onhltptdetamindR_HLT_1","",50,-1,4)
        hist_onhltptdetamindR_HLT_2 = ROOT.TH1D("onhltptdetamindR_HLT_2","",50,-1,4)
        hist_onhltptdetamindR_HLT = ROOT.TH1D("onhltptdetamindR_HLT","",50,-1,4)
        hist_onhltetadetamindR = ROOT.TH1D("onhltetadetamindR","",50,-1,4)
        hist_onhltetadetamindR_L1_1 = ROOT.TH1D("onhltetadetamindR_L1_1","",50,-1,4)
        hist_onhltetadetamindR_L1_2 = ROOT.TH1D("onhltetadetamindR_L1_2","",50,-1,4)
        hist_onhltetadetamindR_L1 = ROOT.TH1D("onhltetadetamindR_L1","",50,-1,4)
        hist_onhltetadetamindR_HLT_1 = ROOT.TH1D("onhltetadetamindR_HLT_1","",50,-1,4)
        hist_onhltetadetamindR_HLT_2 = ROOT.TH1D("onhltetadetamindR_HLT_2","",50,-1,4)
        hist_onhltetadetamindR_HLT = ROOT.TH1D("onhltetadetamindR_HLT","",50,-1,4)

        hist_onhltptM = ROOT.TH1D("onhltptM","",2,0,2)
        hist_onhltptM_L1 = ROOT.TH1D("onhltptM_L1","",2,0,2)
        hist_onhltptM_HLT = ROOT.TH1D("onhltptM_HLT","",2,0,2)
        hist_onhltetaM = ROOT.TH1D("onhltetaM","",2,0,2)
        hist_onhltetaM_L1 = ROOT.TH1D("onhltetaM_L1","",2,0,2)
        hist_onhltetaM_HLT = ROOT.TH1D("onhltetaM_HLT","",2,0,2)

        hist_onhltptMf = ROOT.TH1D("onhltptMf","",1,0,1)
        hist_onhltptMf_L1 = ROOT.TH1D("onhltptMf_L1","",1,0,1)
        hist_onhltptMf_HLT = ROOT.TH1D("onhltptMf_HLT","",1,0,1)
        hist_onhltetaMf = ROOT.TH1D("onhltetaMf","",1,0,1)
        hist_onhltetaMf_L1 = ROOT.TH1D("onhltetaMf_L1","",1,0,1)
        hist_onhltetaMf_HLT = ROOT.TH1D("onhltetaMf_HLT","",1,0,1)

        hist_onhltptnM = ROOT.TH1D("onhltptnM","",5,0,5)
        hist_onhltptnM_L1 = ROOT.TH1D("onhltptnM_L1","",5,0,5)
        hist_onhltptnM_HLT = ROOT.TH1D("onhltptnM_HLT","",5,0,5)
        hist_onhltetanM = ROOT.TH1D("onhltetanM","",5,0,5)
        hist_onhltetanM_L1 = ROOT.TH1D("onhltetanM_L1","",5,0,5)
        hist_onhltetanM_HLT = ROOT.TH1D("onhltetanM_HLT","",5,0,5)

        hist_onhltptnMf = ROOT.TH1D("onhltptnMf","",5,0,5)
        hist_onhltptnMf_L1 = ROOT.TH1D("onhltptnMf_L1","",5,0,5)
        hist_onhltptnMf_HLT = ROOT.TH1D("onhltptnMf_HLT","",5,0,5)
        hist_onhltetanMf = ROOT.TH1D("onhltetanMf","",5,0,5)
        hist_onhltetanMf_L1 = ROOT.TH1D("onhltetanMf_L1","",5,0,5)
        hist_onhltetanMf_HLT = ROOT.TH1D("onhltetanMf_HLT","",5,0,5)

        hist_onhltptnMvsf = ROOT.TH2D("onhltptnMvsf","",5,0,5,5,0,5)
        hist_onhltptnMvsf_L1 = ROOT.TH2D("onhltptnMvsf_L1","",5,0,5,5,0,5)
        hist_onhltptnMvsf_HLT = ROOT.TH2D("onhltptnMvsf_HLT","",5,0,5,5,0,5)
        hist_onhltetanMvsf = ROOT.TH2D("onhltetanMvsf","",5,0,5,5,0,5)
        hist_onhltetanMvsf_L1 = ROOT.TH2D("onhltetanMvsf_L1","",5,0,5,5,0,5)
        hist_onhltetanMvsf_HLT = ROOT.TH2D("onhltetanMvsf_HLT","",5,0,5,5,0,5)

        hist_onhltptnCvsf = ROOT.TH2D("onhltptnCvsf","",5,0,5,5,0,5)
        hist_onhltptnCvsf_L1 = ROOT.TH2D("onhltptnCvsf_L1","",5,0,5,5,0,5)
        hist_onhltptnCvsf_HLT = ROOT.TH2D("onhltptnCvsf_HLT","",5,0,5,5,0,5)
        hist_onhltetanCvsf = ROOT.TH2D("onhltetanCvsf","",5,0,5,5,0,5)
        hist_onhltetanCvsf_L1 = ROOT.TH2D("onhltetanCvsf_L1","",5,0,5,5,0,5)
        hist_onhltetanCvsf_HLT = ROOT.TH2D("onhltetanCvsf_HLT","",5,0,5,5,0,5)

        hist_onhltptndRf = ROOT.TH1D("onhltptndRf","",10,0,10)
        hist_onhltptndRf_L1 = ROOT.TH1D("onhltptndRf_L1","",10,0,10)
        hist_onhltptndRf_HLT = ROOT.TH1D("onhltptndRf_HLT","",10,0,10)
        hist_onhltetandRf = ROOT.TH1D("onhltetandRf","",10,0,10)
        hist_onhltetandRf_L1 = ROOT.TH1D("onhltetandRf_L1","",10,0,10)
        hist_onhltetandRf_HLT = ROOT.TH1D("onhltetandRf_HLT","",10,0,10)

        hist_onMhltptdR01 = ROOT.TH1D("onMhltptdR01","",50,-1,4)
        hist_onMhltptdR01_L1 = ROOT.TH1D("onMhltptdR01_L1","",50,-1,4)
        hist_onMhltptdR01_HLT = ROOT.TH1D("onMhltptdR01_HLT","",50,-1,4)
        hist_onMhltetadR01 = ROOT.TH1D("onMhltetadR01","",50,-1,4)
        hist_onMhltetadR01_L1 = ROOT.TH1D("onMhltetadR01_L1","",50,-1,4)
        hist_onMhltetadR01_HLT = ROOT.TH1D("onMhltetadR01_HLT","",50,-1,4)

        hist_onMhltptdphi01 = ROOT.TH1D("onMhltptdphi01","",50,-1,4)
        hist_onMhltptdphi01_L1 = ROOT.TH1D("onMhltptdphi01_L1","",50,-1,4)
        hist_onMhltptdphi01_HLT = ROOT.TH1D("onMhltptdphi01_HLT","",50,-1,4)
        hist_onMhltetadphi01 = ROOT.TH1D("onMhltetadphi01","",50,-1,4)
        hist_onMhltetadphi01_L1 = ROOT.TH1D("onMhltetadphi01_L1","",50,-1,4)
        hist_onMhltetadphi01_HLT = ROOT.TH1D("onMhltetadphi01_HLT","",50,-1,4)

        hist_onMhltptdeta01 = ROOT.TH1D("onMhltptdeta01","",50,-1,4)
        hist_onMhltptdeta01_L1 = ROOT.TH1D("onMhltptdeta01_L1","",50,-1,4)
        hist_onMhltptdeta01_HLT = ROOT.TH1D("onMhltptdeta01_HLT","",50,-1,4)
        hist_onMhltetadeta01 = ROOT.TH1D("onMhltetadeta01","",50,-1,4)
        hist_onMhltetadeta01_L1 = ROOT.TH1D("onMhltetadeta01_L1","",50,-1,4)
        hist_onMhltetadeta01_HLT = ROOT.TH1D("onMhltetadeta01_HLT","",50,-1,4)

        hist_onhltptpt_VL = ROOT.TH1D("onhltptpt_VL","",200,0,100)
        hist_onhltptpt_L = ROOT.TH1D("onhltptpt_L","",200,0,1000)
        hist_onhltptpt_M = ROOT.TH1D("onhltptpt_M","",200,0,1000)
        hist_onhltptpt_T = ROOT.TH1D("onhltptpt_T","",200,0,1000)

        hist_onhltetapt_VL = ROOT.TH1D("onhltetapt_VL","",200,0,1000)
        hist_onhltetapt_L = ROOT.TH1D("onhltetapt_L","",200,0,1000)
        hist_onhltetapt_M = ROOT.TH1D("onhltetapt_M","",200,0,1000)
        hist_onhltetapt_T = ROOT.TH1D("onhltetapt_T","",200,0,1000)

        hist_onhltpteta = ROOT.TH1D("onhltpteta","",70,-3.5,3.5)
        hist_onhltpteta_VL = ROOT.TH1D("onhltpteta_VL","",70,-3.5,3.5)
        hist_onhltpteta_L = ROOT.TH1D("onhltpteta_L","",70,-3.5,3.5)
        hist_onhltpteta_M = ROOT.TH1D("onhltpteta_M","",70,-3.5,3.5)
        hist_onhltpteta_T = ROOT.TH1D("onhltpteta_T","",70,-3.5,3.5)

        hist_onhltetaeta = ROOT.TH1D("onhltetaeta","",70,-3.5,3.5)
        hist_onhltetaeta_VL = ROOT.TH1D("onhltetaeta_VL","",70,-3.5,3.5)
        hist_onhltetaeta_L = ROOT.TH1D("onhltetaeta_L","",70,-3.5,3.5)
        hist_onhltetaeta_M = ROOT.TH1D("onhltetaeta_M","",70,-3.5,3.5)
        hist_onhltetaeta_T = ROOT.TH1D("onhltetaeta_T","",70,-3.5,3.5)

        hist_onhltptRNNScore = ROOT.TH1D("onhltptRNNScore","",102,-0.01,1.01)
        hist_onhltptRNNScore_VL = ROOT.TH1D("onhltptRNNScore_VL","",102,-0.01,1.01)
        hist_onhltptRNNScore_L = ROOT.TH1D("onhltptRNNScore_L","",102,-0.01,1.01)
        hist_onhltptRNNScore_M = ROOT.TH1D("onhltptRNNScore_M","",102,-0.01,1.01)
        hist_onhltptRNNScore_T = ROOT.TH1D("onhltptRNNScore_T","",102,-0.01,1.01)

        hist_onhltetaRNNScore = ROOT.TH1D("onhltetaRNNScore","",102,-0.01,1.01)
        hist_onhltetaRNNScore_VL = ROOT.TH1D("onhltetaRNNScore_VL","",102,-0.01,1.01)
        hist_onhltetaRNNScore_L = ROOT.TH1D("onhltetaRNNScore_L","",102,-0.01,1.01)
        hist_onhltetaRNNScore_M = ROOT.TH1D("onhltetaRNNScore_M","",102,-0.01,1.01)
        hist_onhltetaRNNScore_T = ROOT.TH1D("onhltetaRNNScore_T","",102,-0.01,1.01)

        hist_onhltptpt_Tf = ROOT.TH1D("onhltptpt_Tf","",200,0,1000)
        hist_onhltptpt_Mf = ROOT.TH1D("onhltptpt_Mf","",200,0,1000)
        hist_onhltptpt_Lf = ROOT.TH1D("onhltptpt_Lf","",200,0,1000)
        hist_onhltptpt_VLf = ROOT.TH1D("onhltptpt_VLf","",200,0,1000)

        hist_onhltetapt_Tf = ROOT.TH1D("onhltetapt_Tf","",200,0,1000)
        hist_onhltetapt_Mf = ROOT.TH1D("onhltetapt_Mf","",200,0,1000)
        hist_onhltetapt_Lf = ROOT.TH1D("onhltetapt_Lf","",200,0,1000)
        hist_onhltetapt_VLf = ROOT.TH1D("onhltetapt_VLf","",200,0,1000)

        #hist_onhltptpt_1200 = ROOT.TH1D("onhltptpt_1200","",200,0,1200)
        #hist_onhltetapt_1200 = ROOT.TH1D("onhltetapt_1200","",200,0,1200)
        hist_onhltptpt_Cf = ROOT.TH1D("onhltptpt_Cf","",200,0,800)
        hist_onhltetapt_Cf = ROOT.TH1D("onhltetapt_Cf","",200,0,800)

        hist_onhltpteta_Tf = ROOT.TH1D("onhltpteta_Tf","",70,-3.5,3.5)
        hist_onhltpteta_Mf = ROOT.TH1D("onhltpteta_Mf","",70,-3.5,3.5)
        hist_onhltpteta_Lf = ROOT.TH1D("onhltpteta_Lf","",70,-3.5,3.5)
        hist_onhltpteta_VLf = ROOT.TH1D("onhltpteta_VLf","",70,-3.5,3.5)

        hist_onhltetaeta_Tf = ROOT.TH1D("onhltetaeta_Tf","",70,-3.5,3.5)
        hist_onhltetaeta_Mf = ROOT.TH1D("onhltetaeta_Mf","",70,-3.5,3.5)
        hist_onhltetaeta_Lf = ROOT.TH1D("onhltetaeta_Lf","",70,-3.5,3.5)
        hist_onhltetaeta_VLf = ROOT.TH1D("onhltetaeta_VLf","",70,-3.5,3.5)

        hist_onhltptRNNScore_Tf = ROOT.TH1D("onhltptRNNScore_Tf","",102,-0.01,1.01)
        hist_onhltptRNNScore_Mf = ROOT.TH1D("onhltptRNNScore_Mf","",102,-0.01,1.01)
        hist_onhltptRNNScore_Lf = ROOT.TH1D("onhltptRNNScore_Lf","",102,-0.01,1.01)
        hist_onhltptRNNScore_VLf = ROOT.TH1D("onhltptRNNScore_VLf","",102,-0.01,1.01)

        hist_onhltetaRNNScore_Tf = ROOT.TH1D("onhltetaRNNScore_Tf","",102,-0.01,1.01)
        hist_onhltetaRNNScore_Mf = ROOT.TH1D("onhltetaRNNScore_Mf","",102,-0.01,1.01)
        hist_onhltetaRNNScore_Lf = ROOT.TH1D("onhltetaRNNScore_Lf","",102,-0.01,1.01)
        hist_onhltetaRNNScore_VLf = ROOT.TH1D("onhltetaRNNScore_VLf","",102,-0.01,1.01)

        entries = xrange(tree.GetEntries())
        for entry in entries:
            if entry % printer == 0: print("Entry: %s/%s." % (entry, len(entries)-1))
            tree.GetEntry(entry)

            i_pt = -1; j_pt = -1; onhltptmindR = 2*math.pi; i_Mpt = -1; j_Mpt = -1; n_pt = 0; n_ptM = 0; n_ptMf = 0; n_ptC = 0; n_ptCf = 0
            for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                n_pt += 1
                hist_onhltptpt.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                hist_onhltptpt_z.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                #hist_onhltptpt_1200.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                hist_onhltpteta.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                hist_onhltptRNNScore.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                if (i == 0):
                    hist_onhltpt0pt.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    hist_onhltpt0pt_z.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                if (i == 1):
                    hist_onhltpt1pt.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                    hist_onhltpt1pt_z.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    for j in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                        if (i != j) and (tree.TrigMatched_Taus_HLTptfl[i].DeltaR(tree.TrigMatched_Taus_HLTptfl[j]) < onhltptmindR):
                            i_pt = i; j_pt = j; onhltptmindR = tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaR(tree.TrigMatched_Taus_HLTptfl[j_pt])
                hist_onhltptM.Fill(tree.TrigMatched_TauIDm_HLTptfl[i],1)
                if tree.TrigMatched_TauIDvl_HLTptfl[i]:
                    hist_onhltptpt_VL.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_VL.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_VL.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                else:
                    hist_onhltptpt_VLf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_VLf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_VLf.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                if tree.TrigMatched_TauIDl_HLTptfl[i]:
                    hist_onhltptpt_L.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_L.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_L.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                else:
                    hist_onhltptpt_Lf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_Lf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_Lf.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                if tree.TrigMatched_TauIDm_HLTptfl[i]:
                    n_ptM += 1
                    hist_onhltptpt_M.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_M.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_M.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                else:
                    hist_onhltptMf.Fill(tree.TrigMatched_TauIDm_HLTptfl[i],1)
                    n_ptMf += 1
                    hist_onhltptpt_Mf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_Mf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    #if taus[t] == "pass":
                        #print("(hltpt_Mf) pt; eta: %s;%s." % (tree.TrigMatched_Taus_HLTptfl[i].Pt(),tree.TrigMatched_Taus_HLTptfl[i].Eta()))
                    hist_onhltptRNNScore_Mf.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                if tree.TrigMatched_TauIDt_HLTptfl[i]:
                    hist_onhltptpt_T.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_T.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_T.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                else:
                    hist_onhltptpt_Tf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltpteta_Tf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Eta(),1)
                    hist_onhltptRNNScore_Tf.Fill(tree.TrigMatched_rnn_HLTptfl[i],1)
                if tree.TrigMatched_HLTptflag[i]:
                    n_ptC += 1
                else:
                    n_ptCf += 1
                    hist_onhltptpt_Cf.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if taus[t] == "pass":
                        print("(hltpt_Mf) pt; eta: %s;%s." % (tree.TrigMatched_Taus_HLTptfl[i].Pt(),tree.TrigMatched_Taus_HLTptfl[i].Eta()))         
                if (j_Mpt == -1) and tree.TrigMatched_TauIDm_HLTptfl[i]:
                    if i_Mpt == -1:
                        i_Mpt = i
                    else: j_Mpt = i
            hist_onhltptnM.Fill(n_ptM,1)
            hist_onhltptnMf.Fill(n_ptMf,1)
            hist_onhltptnMvsf.Fill(n_ptMf,n_ptM,1)
            hist_onhltptnCvsf.Fill(n_ptCf,n_ptC,1)
            if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                hist_onhltptdR01.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                hist_onhltptdphi01.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                hist_onhltptdeta01.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                hist_onhltptmindR.Fill(onhltptmindR,1)
                hist_onhltptdphimindR.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                hist_onhltptdetamindR.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)
                if (tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]) < 0.3) or (tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]) > 3.0):
                    hist_onhltptndRf.Fill(n_pt)
            if j_Mpt != -1:
                hist_onMhltptdR01.Fill(tree.TrigMatched_Taus_HLTptfl[i_Mpt].DeltaR(tree.TrigMatched_Taus_HLTptfl[j_Mpt]),1)
                hist_onMhltptdphi01.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_Mpt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_Mpt])),1)
                hist_onMhltptdeta01.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_Mpt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_Mpt].Eta()),1)

            i_eta = -1; j_eta = -1; onhltetamindR = 2*math.pi; i_Meta = -1; j_Meta =-1; n_eta = 0; n_etaM = 0; n_etaMf = 0; n_etaC = 0; n_etaCf = 0
            for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                n_eta += 1
                hist_onhltetapt.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                hist_onhltetapt_z.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                #hist_onhltetapt_1200.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                hist_onhltetaeta.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                hist_onhltetaRNNScore.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                if (i == 0):
                    hist_onhlteta0pt.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    hist_onhlteta0pt_z.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                if (i == 1):
                    hist_onhlteta1pt.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                    hist_onhlteta1pt_z.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    for j in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                        if (i != j) and (tree.TrigMatched_Taus_HLTetafl[i].DeltaR(tree.TrigMatched_Taus_HLTetafl[j]) < onhltetamindR):
                            i_eta = i; j_eta = j; onhltetamindR = tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaR(tree.TrigMatched_Taus_HLTetafl[j_eta])
                hist_onhltetaM.Fill(tree.TrigMatched_TauIDm_HLTetafl[i],1)
                if tree.TrigMatched_TauIDvl_HLTetafl[i]:
                    hist_onhltetapt_VL.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_VL.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_VL.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                else:
                    hist_onhltetapt_VLf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_VLf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_VLf.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                if tree.TrigMatched_TauIDl_HLTetafl[i]:
                    hist_onhltetapt_L.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_L.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_L.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                else:
                    hist_onhltetapt_Lf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_Lf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_Lf.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                if tree.TrigMatched_TauIDm_HLTetafl[i]:
                    n_etaM += 1
                    hist_onhltetapt_M.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_M.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_M.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                else:
                    hist_onhltetaMf.Fill(tree.TrigMatched_TauIDm_HLTetafl[i],1)
                    n_etaMf += 1
                    hist_onhltetapt_Mf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_Mf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    #if taus[t] == "pass":
                        #print("(hlteta_Mf) pt; eta: %s;%s." % (tree.TrigMatched_Taus_HLTetafl[i].Pt(),tree.TrigMatched_Taus_HLTetafl[i].Eta()))
                    hist_onhltetaRNNScore_Mf.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                if tree.TrigMatched_TauIDt_HLTetafl[i]:
                    hist_onhltetapt_T.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_T.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_T.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                else:
                    hist_onhltetapt_Tf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetaeta_Tf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Eta(),1)
                    hist_onhltetaRNNScore_Tf.Fill(tree.TrigMatched_rnn_HLTetafl[i],1)
                if tree.TrigMatched_HLTetaflag[i]:
                    n_etaC += 1
                else:
                    n_etaCf += 1
                    hist_onhltetapt_Cf.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if taus[t] == "pass":
                        print("(hlteta_Mf) pt; eta: %s;%s." % (tree.TrigMatched_Taus_HLTetafl[i].Pt(),tree.TrigMatched_Taus_HLTetafl[i].Eta()))
                if (j_Meta == -1) and tree.TrigMatched_TauIDm_HLTetafl[i]:
                    if i_Meta == -1:
                        i_Meta = i
                    else: j_Meta = i
            hist_onhltetanM.Fill(n_etaM,1)
            hist_onhltetanMf.Fill(n_etaMf,1)
            hist_onhltetanMvsf.Fill(n_etaMf,n_etaM,1)
            hist_onhltetanCvsf.Fill(n_etaCf,n_etaC,1)
            if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                hist_onhltetadR01.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                hist_onhltetadphi01.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                hist_onhltetadeta01.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                hist_onhltetamindR.Fill(onhltetamindR,1)
                hist_onhltetadphimindR.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                hist_onhltetadetamindR.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)
                if (tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]) < 0.3):
                    hist_onhltetandRf.Fill(n_eta)
            if j_Meta != -1:
                hist_onMhltetadR01.Fill(tree.TrigMatched_Taus_HLTetafl[i_Meta].DeltaR(tree.TrigMatched_Taus_HLTetafl[j_Meta]),1)
                hist_onMhltetadphi01.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_Meta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_Meta])),1)
                hist_onMhltetadeta01.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_Meta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_Meta].Eta()),1)

            L1_1 = getattr(tree, "L1_J25")
            L1_2 = getattr(tree, "L1_ETA25")
            HLT_1 = getattr(tree, "HLT_J25")
            HLT_2 = getattr(tree, "HLT_ETA25")
            cut_L1_1 = L1_1[0]
            cut_L1_2 = L1_2[0]
            cut_HLT_1 = HLT_1[0]
            cut_HLT_2 = HLT_2[0]
            cut_L1 = L1_1[0] or L1_2[0]
            cut_HLT = HLT_1[0] or HLT_2[0]

            hist_L1_1.Fill(int(cut_L1_1),1)
            hist_L1_2.Fill(int(cut_L1_2),1)
            hist_L1.Fill(int(cut_L1),1)
            hist_HLT_1.Fill(int(cut_HLT_1),1)
            hist_HLT_2.Fill(int(cut_HLT_2),1)
            hist_HLT.Fill(int(cut_HLT),1)
    
            if cut_L1_1:
                for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (i == 0): hist_onhltpt0pt_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1): hist_onhltpt1pt_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    hist_onhltptdR01_L1_1.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                    hist_onhltptdphi01_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                    hist_onhltptdeta01_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                    hist_onhltptmindR_L1_1.Fill(onhltptmindR,1)
                    hist_onhltptdphimindR_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                    hist_onhltptdetamindR_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)

                for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt_L1_1.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (i == 0): hist_onhlteta0pt_L1_1.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1): hist_onhlteta1pt_L1_1.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    hist_onhltetadR01_L1_1.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                    hist_onhltetadphi01_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                    hist_onhltetadeta01_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                    hist_onhltetamindR_L1_1.Fill(onhltetamindR,1)
                    hist_onhltetadphimindR_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                    hist_onhltetadetamindR_L1_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)

            if cut_L1_2:
                for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt_L1_2.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (i == 0): hist_onhltpt0pt_L1_2.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1): hist_onhltpt1pt_L1_2.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    hist_onhltptdR01_L1_2.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                    hist_onhltptdphi01_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                    hist_onhltptdeta01_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                    hist_onhltptmindR_L1_2.Fill(onhltptmindR,1)
                    hist_onhltptdphimindR_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                    hist_onhltptdetamindR_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)

                for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (i == 0): hist_onhlteta0pt_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1): hist_onhlteta1pt_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    hist_onhltetadR01_L1_2.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                    hist_onhltetadphi01_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                    hist_onhltetadeta01_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                    hist_onhltetamindR_L1_2.Fill(onhltetamindR,1)
                    hist_onhltetadphimindR_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                    hist_onhltetadetamindR_L1_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)

            if cut_L1:
                for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt_L1.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltptpt_L1_z.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (i == 0):
                        hist_onhltpt0pt_L1.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                        hist_onhltpt0pt_L1_z.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1):
                        hist_onhltpt1pt_L1.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                        hist_onhltpt1pt_L1_z.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                    hist_onhltptM_L1.Fill(tree.TrigMatched_TauIDm_HLTptfl[i],1)
                    if not tree.TrigMatched_TauIDm_HLTptfl[i]: hist_onhltptMf_L1.Fill(tree.TrigMatched_TauIDm_HLTptfl[i],1)
                hist_onhltptnM_L1.Fill(n_ptM,1)
                hist_onhltptnMf_L1.Fill(n_ptMf,1)
                hist_onhltptnMvsf_L1.Fill(n_ptMf,n_ptM,1)
                hist_onhltptnCvsf_L1.Fill(n_ptCf,n_ptC,1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    hist_onhltptdR01_L1.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                    hist_onhltptdphi01_L1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                    hist_onhltptdeta01_L1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                    hist_onhltptmindR_L1.Fill(onhltptmindR,1)
                    hist_onhltptdphimindR_L1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                    hist_onhltptdetamindR_L1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)
                    if (tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]) < 0.3) or (tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]) > 3.0):
                        hist_onhltptndRf_L1.Fill(n_pt)
                if j_Mpt != -1:
                    hist_onMhltptdR01_L1.Fill(tree.TrigMatched_Taus_HLTptfl[i_Mpt].DeltaR(tree.TrigMatched_Taus_HLTptfl[j_Mpt]),1)
                    hist_onMhltptdphi01_L1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_Mpt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_Mpt])),1)
                    hist_onMhltptdeta01_L1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_Mpt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_Mpt].Eta()),1)

                for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt_L1.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetapt_L1_z.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (i == 0):
                        hist_onhlteta0pt_L1.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                        hist_onhlteta0pt_L1_z.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1):
                        hist_onhlteta1pt_L1.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                        hist_onhlteta1pt_L1_z.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                    hist_onhltetaM_L1.Fill(tree.TrigMatched_TauIDm_HLTetafl[i],1)
                    if not tree.TrigMatched_TauIDm_HLTetafl[i]: hist_onhltetaMf_L1.Fill(tree.TrigMatched_TauIDm_HLTetafl[i],1)
                hist_onhltetanM_L1.Fill(n_etaM,1)
                hist_onhltetanMf_L1.Fill(n_etaMf,1)
                hist_onhltetanMvsf_L1.Fill(n_etaMf,n_etaM,1)
                hist_onhltetanCvsf_L1.Fill(n_etaCf,n_etaC,1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    hist_onhltetadR01_L1.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                    hist_onhltetadphi01_L1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                    hist_onhltetadeta01_L1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                    hist_onhltetamindR_L1.Fill(onhltetamindR,1)
                    hist_onhltetadphimindR_L1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                    hist_onhltetadetamindR_L1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)
                    if (tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]) < 0.3):
                        hist_onhltetandRf_L1.Fill(n_eta)
                if j_Meta != -1:
                    hist_onMhltetadR01_L1.Fill(tree.TrigMatched_Taus_HLTetafl[i_Meta].DeltaR(tree.TrigMatched_Taus_HLTetafl[j_Meta]),1)
                    hist_onMhltetadphi01_L1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_Meta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_Meta])),1)
                    hist_onMhltetadeta01_L1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_Meta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_Meta].Eta()),1)

            if cut_HLT_1:
                for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (i == 0): hist_onhltpt0pt_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1): hist_onhltpt1pt_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    hist_onhltptdR01_HLT_1.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                    hist_onhltptdphi01_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                    hist_onhltptdeta01_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                    hist_onhltptmindR_HLT_1.Fill(onhltptmindR,1)
                    hist_onhltptdphimindR_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                    hist_onhltptdetamindR_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)

                for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt_HLT_1.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (i == 0): hist_onhlteta0pt_HLT_1.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1): hist_onhlteta1pt_HLT_1.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    hist_onhltetadR01_HLT_1.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                    hist_onhltetadphi01_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                    hist_onhltetadeta01_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                    hist_onhltetamindR_HLT_1.Fill(onhltetamindR,1)
                    hist_onhltetadphimindR_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                    hist_onhltetadetamindR_HLT_1.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)

            if cut_HLT_2:
                for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt_HLT_2.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (i == 0): hist_onhltpt0pt_HLT_2.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1): hist_onhltpt1pt_HLT_2.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    hist_onhltptdR01_HLT_2.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                    hist_onhltptdphi01_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                    hist_onhltptdeta01_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                    hist_onhltptmindR_HLT_2.Fill(onhltptmindR,1)
                    hist_onhltptdphimindR_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                    hist_onhltptdetamindR_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)

                for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (i == 0): hist_onhlteta0pt_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1): hist_onhlteta1pt_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    hist_onhltetadR01_HLT_2.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                    hist_onhltetadphi01_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                    hist_onhltetadeta01_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                    hist_onhltetamindR_HLT_2.Fill(onhltetamindR,1)
                    hist_onhltetadphimindR_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                    hist_onhltetadetamindR_HLT_2.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)

            if cut_HLT:
                for i in xrange(len(tree.TrigMatched_Taus_HLTptfl)):
                    hist_onhltptpt_HLT.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    hist_onhltptpt_HLT_z.Fill(tree.TrigMatched_Taus_HLTptfl[i].Pt(),1)
                    if (i == 0):
                        hist_onhltpt0pt_HLT.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                        hist_onhltpt0pt_HLT_z.Fill(tree.TrigMatched_Taus_HLTptfl[0].Pt(),1)
                    if (i == 1):
                        hist_onhltpt1pt_HLT.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                        hist_onhltpt1pt_HLT_z.Fill(tree.TrigMatched_Taus_HLTptfl[1].Pt(),1)
                    hist_onhltptM_HLT.Fill(tree.TrigMatched_TauIDm_HLTptfl[i],1)
                    if not tree.TrigMatched_TauIDm_HLTptfl[i]: hist_onhltptMf_HLT.Fill(tree.TrigMatched_TauIDm_HLTptfl[i],1)
                hist_onhltptnM_HLT.Fill(n_ptM,1)
                hist_onhltptnMf_HLT.Fill(n_ptMf,1)
                hist_onhltptnMvsf_HLT.Fill(n_ptMf,n_ptM,1)
                hist_onhltptnCvsf_HLT.Fill(n_ptCf,n_ptC,1)
                if len(tree.TrigMatched_Taus_HLTptfl) > 1:
                    hist_onhltptdR01_HLT.Fill(tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]),1)
                    hist_onhltptdphi01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[1])),1)
                    hist_onhltptdeta01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTptfl[0].Eta()-tree.TrigMatched_Taus_HLTptfl[1].Eta()),1)
                    hist_onhltptmindR_HLT.Fill(onhltptmindR,1)
                    hist_onhltptdphimindR_HLT.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_pt])),1)
                    hist_onhltptdetamindR_HLT.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_pt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_pt].Eta()),1)
                    if (tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]) < 0.3) or (tree.TrigMatched_Taus_HLTptfl[0].DeltaR(tree.TrigMatched_Taus_HLTptfl[1]) > 3.0):
                        hist_onhltptndRf_HLT.Fill(n_pt)
                if j_Mpt != -1:
                    hist_onMhltptdR01_HLT.Fill(tree.TrigMatched_Taus_HLTptfl[i_Mpt].DeltaR(tree.TrigMatched_Taus_HLTptfl[j_Mpt]),1)
                    hist_onMhltptdphi01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_Mpt].DeltaPhi(tree.TrigMatched_Taus_HLTptfl[j_Mpt])),1)
                    hist_onMhltptdeta01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTptfl[i_Mpt].Eta()-tree.TrigMatched_Taus_HLTptfl[j_Mpt].Eta()),1)

                for i in xrange(len(tree.TrigMatched_Taus_HLTetafl)):
                    hist_onhltetapt_HLT.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    hist_onhltetapt_HLT_z.Fill(tree.TrigMatched_Taus_HLTetafl[i].Pt(),1)
                    if (i == 0):
                        hist_onhlteta0pt_HLT.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                        hist_onhlteta0pt_HLT_z.Fill(tree.TrigMatched_Taus_HLTetafl[0].Pt(),1)
                    if (i == 1):
                        hist_onhlteta1pt_HLT.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                        hist_onhlteta1pt_HLT_z.Fill(tree.TrigMatched_Taus_HLTetafl[1].Pt(),1)
                    hist_onhltetaM_HLT.Fill(tree.TrigMatched_TauIDm_HLTetafl[i],1)
                    if not tree.TrigMatched_TauIDm_HLTetafl[i]: hist_onhltetaMf_HLT.Fill(tree.TrigMatched_TauIDm_HLTetafl[i],1)
                hist_onhltetanM_HLT.Fill(n_etaM,1)
                hist_onhltetanMf_HLT.Fill(n_etaMf,1)
                hist_onhltetanMvsf_HLT.Fill(n_etaMf,n_etaM,1)
                hist_onhltetanCvsf_HLT.Fill(n_etaCf,n_etaC,1)
                if len(tree.TrigMatched_Taus_HLTetafl) > 1:
                    hist_onhltetadR01_HLT.Fill(tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]),1)
                    hist_onhltetadphi01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[1])),1)
                    hist_onhltetadeta01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTetafl[0].Eta()-tree.TrigMatched_Taus_HLTetafl[1].Eta()),1)
                    hist_onhltetamindR_HLT.Fill(onhltetamindR,1)
                    hist_onhltetadphimindR_HLT.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_eta])),1)
                    hist_onhltetadetamindR_HLT.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_eta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_eta].Eta()),1)
                    if (tree.TrigMatched_Taus_HLTetafl[0].DeltaR(tree.TrigMatched_Taus_HLTetafl[1]) < 0.3):
                        hist_onhltetandRf_HLT.Fill(n_eta)
                if j_Meta != -1:
                    hist_onMhltetadR01_HLT.Fill(tree.TrigMatched_Taus_HLTetafl[i_Meta].DeltaR(tree.TrigMatched_Taus_HLTetafl[j_Meta]),1)
                    hist_onMhltetadphi01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_Meta].DeltaPhi(tree.TrigMatched_Taus_HLTetafl[j_Meta])),1)
                    hist_onMhltetadeta01_HLT.Fill(abs(tree.TrigMatched_Taus_HLTetafl[i_Meta].Eta()-tree.TrigMatched_Taus_HLTetafl[j_Meta].Eta()),1)

        hists_L1 = [hist_L1_1, hist_L1_2, hist_L1]
        hists_HLT = [hist_HLT_1, hist_HLT_2, hist_HLT]
        diff = ["_{1}", "_{2}", ""]
        diffpng = ["1", "2", ""]
        for h in range(len(hists_L1)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            hists_L1[h].Draw()
            hists_L1[h].SetLineColor(ROOT.kBlue)
            hists_L1[h].SetLineWidth(2)
            hists_HLT[h].Draw("SAME")
            hists_HLT[h].SetLineColor(ROOT.kRed)
            hists_HLT[h].SetLineWidth(1)
            hists_L1[h].SetTitle(";Triggers;")
            hists_L1[h].GetYaxis().SetTitleOffset(1.05)
            hists_L1[h].SetMinimum(0.9*min(hists_L1[h].GetMinimum(),hists_HLT[h].GetMinimum()))
            hists_L1[h].SetMaximum(1.1*max(hists_L1[h].GetMaximum(),hists_HLT[h].GetMaximum()))
            hists_L1[h].SetNdivisions(2)
            legend = ROOT.TLegend(0.675,0.45,0.95,0.60)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_L1[h],"Pass L1"+diff[h]+" ("+str(int(hists_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_HLT[h],"Pass HLT"+diff[h]+" ("+str(int(hists_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"trg"+diffpng[h]+".png")
            canvas.Close()

        hists_onhltptpt = [hist_onhltptpt, hist_onhltpt0pt, hist_onhltpt1pt]
        hists_onhltptpt_L1_1 = [hist_onhltptpt_L1_1, hist_onhltpt0pt_L1_1, hist_onhltpt1pt_L1_1]
        hists_onhltptpt_HLT_1 = [hist_onhltptpt_HLT_1, hist_onhltpt0pt_HLT_1, hist_onhltpt1pt_HLT_1]
        diff = ["", "lead", "subl"]
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
            hists_onhltptpt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltptpt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltptpt[h].SetAxisRange(0,500,"X")
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
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

        hists_onhltptpt = [hist_onhltptpt, hist_onhltpt0pt, hist_onhltpt1pt]
        hists_onhltptpt_L1_2 = [hist_onhltptpt_L1_2, hist_onhltpt0pt_L1_2, hist_onhltpt1pt_L1_2]
        hists_onhltptpt_HLT_2 = [hist_onhltptpt_HLT_2, hist_onhltpt0pt_HLT_2, hist_onhltpt1pt_HLT_2]
        diff = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltptpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltptpt[h].Draw()
            hists_onhltptpt[h].SetLineColor(ROOT.kBlack)
            hists_onhltptpt[h].SetLineWidth(3)
            hists_onhltptpt_L1_2[h].Draw("same")
            hists_onhltptpt_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltptpt_L1_2[h].SetLineWidth(2)
            hists_onhltptpt_HLT_2[h].Draw("same")
            hists_onhltptpt_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltptpt_HLT_2[h].SetLineWidth(1)
            hists_onhltptpt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltptpt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltptpt[h].SetAxisRange(0,500,"X")
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltptpt[h],"Tau hltpt ("+str(int(hists_onhltptpt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltptpt_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltptpt_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhltpt"+diffpng[h]+"pttrg2.png")
            canvas.Close()
    
        hists_onhltptpt = [hist_onhltptpt, hist_onhltpt0pt, hist_onhltpt1pt]
        hists_onhltptpt_L1 = [hist_onhltptpt_L1, hist_onhltpt0pt_L1, hist_onhltpt1pt_L1]
        hists_onhltptpt_HLT = [hist_onhltptpt_HLT, hist_onhltpt0pt_HLT, hist_onhltpt1pt_HLT]
        diff = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltptpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltptpt[h].Draw()
            hists_onhltptpt[h].SetLineColor(ROOT.kBlack)
            hists_onhltptpt[h].SetLineWidth(3)
            hists_onhltptpt_L1[h].Draw("same")
            hists_onhltptpt_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltptpt_L1[h].SetLineWidth(2)
            hists_onhltptpt_HLT[h].Draw("same")
            hists_onhltptpt_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltptpt_HLT[h].SetLineWidth(1)
            hists_onhltptpt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltptpt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltptpt[h].SetAxisRange(0,500,"X")
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltptpt[h],"Tau hltpt ("+str(int(hists_onhltptpt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_L1[h],"Pass L1 ("+str(int(hists_onhltptpt_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_HLT[h],"Pass HLT ("+str(int(hists_onhltptpt_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhltpt"+diffpng[h]+"pt.png")
            canvas.Close()

        hists_onhltetapt = [hist_onhltetapt, hist_onhlteta0pt, hist_onhlteta1pt]
        hists_onhltetapt_L1_1 = [hist_onhltetapt_L1_1, hist_onhlteta0pt_L1_1, hist_onhlteta1pt_L1_1]
        hists_onhltetapt_HLT_1 = [hist_onhltetapt_HLT_1, hist_onhlteta0pt_HLT_1, hist_onhlteta1pt_HLT_1]
        diff = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltetapt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltetapt[h].Draw()
            hists_onhltetapt[h].SetLineColor(ROOT.kBlack)
            hists_onhltetapt[h].SetLineWidth(3)
            hists_onhltetapt_L1_1[h].Draw("same")
            hists_onhltetapt_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltetapt_L1_1[h].SetLineWidth(2)
            hists_onhltetapt_HLT_1[h].Draw("same")
            hists_onhltetapt_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltetapt_HLT_1[h].SetLineWidth(1)
            hists_onhltetapt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltetapt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltetapt[h].SetAxisRange(0,500,"X")
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltetapt[h],"Tau hlteta ("+str(int(hists_onhltetapt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltetapt_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltetapt_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhlteta"+diffpng[h]+"pttrg1.png")
            canvas.Close()

        hists_onhltetapt = [hist_onhltetapt, hist_onhlteta0pt, hist_onhlteta1pt]
        hists_onhltetapt_L1_2 = [hist_onhltetapt_L1_2, hist_onhlteta0pt_L1_2, hist_onhlteta1pt_L1_2]
        hists_onhltetapt_HLT_2 = [hist_onhltetapt_HLT_2, hist_onhlteta0pt_HLT_2, hist_onhlteta1pt_HLT_2]
        diff = ["", "lead", "subl"]
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
            hists_onhltetapt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltetapt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltetapt[h].SetAxisRange(0,500,"X")
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
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

        hists_onhltetapt = [hist_onhltetapt, hist_onhlteta0pt, hist_onhlteta1pt]
        hists_onhltetapt_L1 = [hist_onhltetapt_L1, hist_onhlteta0pt_L1, hist_onhlteta1pt_L1]
        hists_onhltetapt_HLT = [hist_onhltetapt_HLT, hist_onhlteta0pt_HLT, hist_onhlteta1pt_HLT]
        diff = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltetapt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltetapt[h].Draw()
            hists_onhltetapt[h].SetLineColor(ROOT.kBlack)
            hists_onhltetapt[h].SetLineWidth(3)
            hists_onhltetapt_L1[h].Draw("same")
            hists_onhltetapt_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltetapt_L1[h].SetLineWidth(2)
            hists_onhltetapt_HLT[h].Draw("same")
            hists_onhltetapt_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltetapt_HLT[h].SetLineWidth(1)
            hists_onhltetapt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltetapt[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltetapt[h].SetAxisRange(0,500,"X")
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltetapt[h],"Tau hlteta ("+str(int(hists_onhltetapt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_L1[h],"Pass L1 ("+str(int(hists_onhltetapt_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_HLT[h],"Pass HLT ("+str(int(hists_onhltetapt_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhlteta"+diffpng[h]+"pt.png")
            canvas.Close()

        hists_onhltptpt_z = [hist_onhltptpt_z, hist_onhltpt0pt_z, hist_onhltpt1pt_z]
        hists_onhltptpt_L1_z = [hist_onhltptpt_L1_z, hist_onhltpt0pt_L1_z, hist_onhltpt1pt_L1_z]
        hists_onhltptpt_HLT_z = [hist_onhltptpt_HLT_z, hist_onhltpt0pt_HLT_z, hist_onhltpt1pt_HLT_z]
        diff = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltptpt_z)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltptpt_z[h].Draw()
            hists_onhltptpt_z[h].SetLineColor(ROOT.kBlack)
            hists_onhltptpt_z[h].SetLineWidth(3)
            hists_onhltptpt_L1_z[h].Draw("same")
            hists_onhltptpt_L1_z[h].SetLineColor(ROOT.kBlue)
            hists_onhltptpt_L1_z[h].SetLineWidth(2)
            hists_onhltptpt_HLT_z[h].Draw("same")
            hists_onhltptpt_HLT_z[h].SetLineColor(ROOT.kRed)
            hists_onhltptpt_HLT_z[h].SetLineWidth(1)
            hists_onhltptpt_z[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltptpt_z[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltptpt_z[h].SetMinimum(1)
            l_x_min = l_x_min_L
            l_x_max = l_x_max_L
            if diff[h] == "subl":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltptpt_z[h],"Tau hltpt ("+str(int(hists_onhltptpt_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_L1_z[h],"Pass L1 ("+str(int(hists_onhltptpt_L1_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltptpt_HLT_z[h],"Pass HLT ("+str(int(hists_onhltptpt_HLT_z[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhltpt"+diffpng[h]+"ptz.png")
            canvas.Close()

        hists_onhltetapt_z = [hist_onhltetapt_z, hist_onhlteta0pt_z, hist_onhlteta1pt_z]
        hists_onhltetapt_L1_z = [hist_onhltetapt_L1_z, hist_onhlteta0pt_L1_z, hist_onhlteta1pt_L1_z]
        hists_onhltetapt_HLT_z = [hist_onhltetapt_HLT_z, hist_onhlteta0pt_HLT_z, hist_onhlteta1pt_HLT_z]
        diff = ["", "lead", "subl"]
        diffpng = ["", "0", "1"]
        for h in range(len(hists_onhltetapt_z)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltetapt_z[h].Draw()
            hists_onhltetapt_z[h].SetLineColor(ROOT.kBlack)
            hists_onhltetapt_z[h].SetLineWidth(3)
            hists_onhltetapt_L1_z[h].Draw("same")
            hists_onhltetapt_L1_z[h].SetLineColor(ROOT.kBlue)
            hists_onhltetapt_L1_z[h].SetLineWidth(2)
            hists_onhltetapt_HLT_z[h].Draw("same")
            hists_onhltetapt_HLT_z[h].SetLineColor(ROOT.kRed)
            hists_onhltetapt_HLT_z[h].SetLineWidth(1)
            hists_onhltetapt_z[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltetapt_z[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltetapt_z[h].SetMinimum(1)
            l_x_min = l_x_min_L
            l_x_max = l_x_max_L
            if diff[h] == "subl":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltetapt_z[h],"Tau hlteta ("+str(int(hists_onhltetapt_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_L1_z[h],"Pass L1 ("+str(int(hists_onhltetapt_L1_z[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltetapt_HLT_z[h],"Pass HLT ("+str(int(hists_onhltetapt_HLT_z[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onhlteta"+diffpng[h]+"ptz.png")
            canvas.Close()

        hists_onhltdR01 = [hist_onhltptdR01, hist_onhltetadR01]
        hists_onhltdR01_L1_1 = [hist_onhltptdR01_L1_1, hist_onhltetadR01_L1_1]
        hists_onhltdR01_HLT_1 = [hist_onhltptdR01_HLT_1, hist_onhltetadR01_HLT_1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdR01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdR01[h].Draw()
            hists_onhltdR01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdR01[h].SetLineWidth(3)
            hists_onhltdR01_L1_1[h].Draw("same")
            hists_onhltdR01_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdR01_L1_1[h].SetLineWidth(2)
            hists_onhltdR01_HLT_1[h].Draw("same")
            hists_onhltdR01_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltdR01_HLT_1[h].SetLineWidth(1)
            hists_onhltdR01[h].SetTitle(";dR;Online dR(lead#tau,subl#tau)")
            hists_onhltdR01[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdR01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdR01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdR01_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltdR01_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdR01_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltdR01_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dR01trg1.png")
            canvas.Close()

        hists_onhltdR01 = [hist_onhltptdR01, hist_onhltetadR01]
        hists_onhltdR01_L1_2 = [hist_onhltptdR01_L1_2, hist_onhltetadR01_L1_2]
        hists_onhltdR01_HLT_2 = [hist_onhltptdR01_HLT_2, hist_onhltetadR01_HLT_2]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdR01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdR01[h].Draw()
            hists_onhltdR01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdR01[h].SetLineWidth(3)
            hists_onhltdR01_L1_2[h].Draw("same")
            hists_onhltdR01_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltdR01_L1_2[h].SetLineWidth(2)
            hists_onhltdR01_HLT_2[h].Draw("same")
            hists_onhltdR01_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltdR01_HLT_2[h].SetLineWidth(1)
            hists_onhltdR01[h].SetTitle(";dR;Online dR(lead#tau,subl#tau)")
            hists_onhltdR01[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdR01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdR01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdR01_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltdR01_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdR01_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltdR01_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dR01trg2.png")
            canvas.Close()
            
        hists_onhltdR01 = [hist_onhltptdR01, hist_onhltetadR01]
        hists_onhltdR01_L1 = [hist_onhltptdR01_L1, hist_onhltetadR01_L1]
        hists_onhltdR01_HLT = [hist_onhltptdR01_HLT, hist_onhltetadR01_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdR01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdR01[h].Draw()
            hists_onhltdR01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdR01[h].SetLineWidth(3)
            hists_onhltdR01_L1[h].Draw("same")
            hists_onhltdR01_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdR01_L1[h].SetLineWidth(2)
            hists_onhltdR01_HLT[h].Draw("same")
            hists_onhltdR01_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltdR01_HLT[h].SetLineWidth(1)
            hists_onhltdR01[h].SetTitle(";dR;Online dR(lead#tau,subl#tau)")
            hists_onhltdR01[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdR01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdR01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdR01_L1[h],"Pass L1 ("+str(int(hists_onhltdR01_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdR01_HLT[h],"Pass HLT ("+str(int(hists_onhltdR01_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dR01.png")
            canvas.Close()

        hists_onhltdphi01 = [hist_onhltptdphi01, hist_onhltetadphi01]
        hists_onhltdphi01_L1_1 = [hist_onhltptdphi01_L1_1, hist_onhltetadphi01_L1_1]
        hists_onhltdphi01_HLT_1 = [hist_onhltptdphi01_HLT_1, hist_onhltetadphi01_HLT_1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdphi01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdphi01[h].Draw()
            hists_onhltdphi01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdphi01[h].SetLineWidth(3)
            hists_onhltdphi01_L1_1[h].Draw("same")
            hists_onhltdphi01_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdphi01_L1_1[h].SetLineWidth(2)
            hists_onhltdphi01_HLT_1[h].Draw("same")
            hists_onhltdphi01_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltdphi01_HLT_1[h].SetLineWidth(1)
            hists_onhltdphi01[h].SetTitle(";|dphi|;Online |dphi(lead#tau,subl#tau)|")
            hists_onhltdphi01[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdphi01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdphi01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphi01_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltdphi01_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphi01_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltdphi01_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dphi01trg1.png")
            canvas.Close()

        hists_onhltdphi01 = [hist_onhltptdphi01, hist_onhltetadphi01]
        hists_onhltdphi01_L1_2 = [hist_onhltptdphi01_L1_2, hist_onhltetadphi01_L1_2]
        hists_onhltdphi01_HLT_2 = [hist_onhltptdphi01_HLT_2, hist_onhltetadphi01_HLT_2]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdphi01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdphi01[h].Draw()
            hists_onhltdphi01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdphi01[h].SetLineWidth(3)
            hists_onhltdphi01_L1_2[h].Draw("same")
            hists_onhltdphi01_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltdphi01_L1_2[h].SetLineWidth(2)
            hists_onhltdphi01_HLT_2[h].Draw("same")
            hists_onhltdphi01_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltdphi01_HLT_2[h].SetLineWidth(1)
            hists_onhltdphi01[h].SetTitle(";|dphi|;Online |dphi(lead#tau,subl#tau)|")
            hists_onhltdphi01[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdphi01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdphi01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphi01_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltdphi01_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphi01_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltdphi01_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dphi01trg2.png")
            canvas.Close()

        hists_onhltdphi01 = [hist_onhltptdphi01, hist_onhltetadphi01]
        hists_onhltdphi01_L1 = [hist_onhltptdphi01_L1, hist_onhltetadphi01_L1]
        hists_onhltdphi01_HLT = [hist_onhltptdphi01_HLT, hist_onhltetadphi01_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdphi01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdphi01[h].Draw()
            hists_onhltdphi01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdphi01[h].SetLineWidth(3)
            hists_onhltdphi01_L1[h].Draw("same")
            hists_onhltdphi01_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdphi01_L1[h].SetLineWidth(2)
            hists_onhltdphi01_HLT[h].Draw("same")
            hists_onhltdphi01_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltdphi01_HLT[h].SetLineWidth(1)
            hists_onhltdphi01[h].SetTitle(";|dphi|;Online |dphi(lead#tau,subl#tau)|")
            hists_onhltdphi01[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdphi01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdphi01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphi01_L1[h],"Pass L1 ("+str(int(hists_onhltdphi01_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphi01_HLT[h],"Pass HLT ("+str(int(hists_onhltdphi01_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dphi01.png")
            canvas.Close()

        hists_onhltdeta01 = [hist_onhltptdeta01, hist_onhltetadeta01]
        hists_onhltdeta01_L1_1 = [hist_onhltptdeta01_L1_1, hist_onhltetadeta01_L1_1]
        hists_onhltdeta01_HLT_1 = [hist_onhltptdeta01_HLT_1, hist_onhltetadeta01_HLT_1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdeta01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdeta01[h].Draw()
            hists_onhltdeta01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdeta01[h].SetLineWidth(3)
            hists_onhltdeta01_L1_1[h].Draw("same")
            hists_onhltdeta01_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdeta01_L1_1[h].SetLineWidth(2)
            hists_onhltdeta01_HLT_1[h].Draw("same")
            hists_onhltdeta01_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltdeta01_HLT_1[h].SetLineWidth(1)
            hists_onhltdeta01[h].SetTitle(";deta;Online deta(lead#tau,subl#tau)")
            hists_onhltdeta01[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdeta01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdeta01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdeta01_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltdeta01_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdeta01_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltdeta01_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"deta01trg1.png")
            canvas.Close()

        hists_onhltdeta01 = [hist_onhltptdeta01, hist_onhltetadeta01]
        hists_onhltdeta01_L1_2 = [hist_onhltptdeta01_L1_2, hist_onhltetadeta01_L1_2]
        hists_onhltdeta01_HLT_2 = [hist_onhltptdeta01_HLT_2, hist_onhltetadeta01_HLT_2]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdeta01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdeta01[h].Draw()
            hists_onhltdeta01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdeta01[h].SetLineWidth(3)
            hists_onhltdeta01_L1_2[h].Draw("same")
            hists_onhltdeta01_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltdeta01_L1_2[h].SetLineWidth(2)
            hists_onhltdeta01_HLT_2[h].Draw("same")
            hists_onhltdeta01_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltdeta01_HLT_2[h].SetLineWidth(1)
            hists_onhltdeta01[h].SetTitle(";deta;Online deta(lead#tau,subl#tau)")
            hists_onhltdeta01[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdeta01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdeta01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdeta01_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltdeta01_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdeta01_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltdeta01_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"deta01trg2.png")
            canvas.Close()

        hists_onhltdeta01 = [hist_onhltptdeta01, hist_onhltetadeta01]
        hists_onhltdeta01_L1 = [hist_onhltptdeta01_L1, hist_onhltetadeta01_L1]
        hists_onhltdeta01_HLT = [hist_onhltptdeta01_HLT, hist_onhltetadeta01_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdeta01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdeta01[h].Draw()
            hists_onhltdeta01[h].SetLineColor(ROOT.kBlack)
            hists_onhltdeta01[h].SetLineWidth(3)
            hists_onhltdeta01_L1[h].Draw("same")
            hists_onhltdeta01_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdeta01_L1[h].SetLineWidth(2)
            hists_onhltdeta01_HLT[h].Draw("same")
            hists_onhltdeta01_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltdeta01_HLT[h].SetLineWidth(1)
            hists_onhltdeta01[h].SetTitle(";deta;Online deta(lead#tau,subl#tau)")
            hists_onhltdeta01[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdeta01[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdeta01[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdeta01_L1[h],"Pass L1 ("+str(int(hists_onhltdeta01_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdeta01_HLT[h],"Pass HLT ("+str(int(hists_onhltdeta01_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"deta01.png")
            canvas.Close()

        hists_onhltmindR = [hist_onhltptmindR, hist_onhltetamindR]
        hists_onhltmindR_L1_1 = [hist_onhltptmindR_L1_1, hist_onhltetamindR_L1_1]
        hists_onhltmindR_HLT_1 = [hist_onhltptmindR_HLT_1, hist_onhltetamindR_HLT_1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltmindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltmindR[h].Draw()
            hists_onhltmindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltmindR[h].SetLineWidth(3)
            hists_onhltmindR_L1_1[h].Draw("same")
            hists_onhltmindR_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltmindR_L1_1[h].SetLineWidth(2)
            hists_onhltmindR_HLT_1[h].Draw("same")
            hists_onhltmindR_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltmindR_HLT_1[h].SetLineWidth(1)
            hists_onhltmindR[h].SetTitle(";dR;Online min dR")
            hists_onhltmindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltmindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltmindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltmindR_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltmindR_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltmindR_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltmindR_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"mindRtrg1.png")
            canvas.Close()

        hists_onhltmindR = [hist_onhltptmindR, hist_onhltetamindR]
        hists_onhltmindR_L1_2 = [hist_onhltptmindR_L1_2, hist_onhltetamindR_L1_2]
        hists_onhltmindR_HLT_2 = [hist_onhltptmindR_HLT_2, hist_onhltetamindR_HLT_2]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltmindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltmindR[h].Draw()
            hists_onhltmindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltmindR[h].SetLineWidth(3)
            hists_onhltmindR_L1_2[h].Draw("same")
            hists_onhltmindR_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltmindR_L1_2[h].SetLineWidth(2)
            hists_onhltmindR_HLT_2[h].Draw("same")
            hists_onhltmindR_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltmindR_HLT_2[h].SetLineWidth(1)
            hists_onhltmindR[h].SetTitle(";dR;Online min dR")
            hists_onhltmindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltmindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltmindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltmindR_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltmindR_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltmindR_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltmindR_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"mindRtrg2.png")
            canvas.Close()

        hists_onhltmindR = [hist_onhltptmindR, hist_onhltetamindR]
        hists_onhltmindR_L1 = [hist_onhltptmindR_L1, hist_onhltetamindR_L1]
        hists_onhltmindR_HLT = [hist_onhltptmindR_HLT, hist_onhltetamindR_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltmindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltmindR[h].Draw()
            hists_onhltmindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltmindR[h].SetLineWidth(3)
            hists_onhltmindR_L1[h].Draw("same")
            hists_onhltmindR_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltmindR_L1[h].SetLineWidth(2)
            hists_onhltmindR_HLT[h].Draw("same")
            hists_onhltmindR_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltmindR_HLT[h].SetLineWidth(1)
            hists_onhltmindR[h].SetTitle(";dR;Online min dR")
            hists_onhltmindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltmindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltmindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltmindR_L1[h],"Pass L1 ("+str(int(hists_onhltmindR_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltmindR_HLT[h],"Pass HLT ("+str(int(hists_onhltmindR_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"mindR.png")
            canvas.Close()

        hists_onhltdphimindR = [hist_onhltptdphimindR, hist_onhltetadphimindR]
        hists_onhltdphimindR_L1_1 = [hist_onhltptdphimindR_L1_1, hist_onhltetadphimindR_L1_1]
        hists_onhltdphimindR_HLT_1 = [hist_onhltptdphimindR_HLT_1, hist_onhltetadphimindR_HLT_1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdphimindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdphimindR[h].Draw()
            hists_onhltdphimindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltdphimindR[h].SetLineWidth(3)
            hists_onhltdphimindR_L1_1[h].Draw("same")
            hists_onhltdphimindR_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdphimindR_L1_1[h].SetLineWidth(2)
            hists_onhltdphimindR_HLT_1[h].Draw("same")
            hists_onhltdphimindR_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltdphimindR_HLT_1[h].SetLineWidth(1)
            hists_onhltdphimindR[h].SetTitle(";|dphi|;Online |dphi(min dR)|")
            hists_onhltdphimindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdphimindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdphimindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphimindR_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltdphimindR_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphimindR_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltdphimindR_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dphimindRtrg1.png")
            canvas.Close()

        hists_onhltdphimindR = [hist_onhltptdphimindR, hist_onhltetadphimindR]
        hists_onhltdphimindR_L1_2 = [hist_onhltptdphimindR_L1_2, hist_onhltetadphimindR_L1_2]
        hists_onhltdphimindR_HLT_2 = [hist_onhltptdphimindR_HLT_2, hist_onhltetadphimindR_HLT_2]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdphimindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdphimindR[h].Draw()
            hists_onhltdphimindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltdphimindR[h].SetLineWidth(3)
            hists_onhltdphimindR_L1_2[h].Draw("same")
            hists_onhltdphimindR_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltdphimindR_L1_2[h].SetLineWidth(2)
            hists_onhltdphimindR_HLT_2[h].Draw("same")
            hists_onhltdphimindR_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltdphimindR_HLT_2[h].SetLineWidth(1)
            hists_onhltdphimindR[h].SetTitle(";|dphi|;Online |dphi(min dR)|")
            hists_onhltdphimindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdphimindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdphimindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphimindR_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltdphimindR_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphimindR_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltdphimindR_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dphimindRtrg2.png")
            canvas.Close()

        hists_onhltdphimindR = [hist_onhltptdphimindR, hist_onhltetadphimindR]
        hists_onhltdphimindR_L1 = [hist_onhltptdphimindR_L1, hist_onhltetadphimindR_L1]
        hists_onhltdphimindR_HLT = [hist_onhltptdphimindR_HLT, hist_onhltetadphimindR_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdphimindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdphimindR[h].Draw()
            hists_onhltdphimindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltdphimindR[h].SetLineWidth(3)
            hists_onhltdphimindR_L1[h].Draw("same")
            hists_onhltdphimindR_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdphimindR_L1[h].SetLineWidth(2)
            hists_onhltdphimindR_HLT[h].Draw("same")
            hists_onhltdphimindR_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltdphimindR_HLT[h].SetLineWidth(1)
            hists_onhltdphimindR[h].SetTitle(";|dphi|;Online |dphi(min dR)|")
            hists_onhltdphimindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdphimindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdphimindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphimindR_L1[h],"Pass L1 ("+str(int(hists_onhltdphimindR_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdphimindR_HLT[h],"Pass HLT ("+str(int(hists_onhltdphimindR_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"dphimindR.png")
            canvas.Close()

        hists_onhltdetamindR = [hist_onhltptdetamindR, hist_onhltetadetamindR]
        hists_onhltdetamindR_L1_1 = [hist_onhltptdetamindR_L1_1, hist_onhltetadetamindR_L1_1]
        hists_onhltdetamindR_HLT_1 = [hist_onhltptdetamindR_HLT_1, hist_onhltetadetamindR_HLT_1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdetamindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdetamindR[h].Draw()
            hists_onhltdetamindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltdetamindR[h].SetLineWidth(3)
            hists_onhltdetamindR_L1_1[h].Draw("same")
            hists_onhltdetamindR_L1_1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdetamindR_L1_1[h].SetLineWidth(2)
            hists_onhltdetamindR_HLT_1[h].Draw("same")
            hists_onhltdetamindR_HLT_1[h].SetLineColor(ROOT.kRed)
            hists_onhltdetamindR_HLT_1[h].SetLineWidth(1)
            hists_onhltdetamindR[h].SetTitle(";deta;Online deta(min dR)")
            hists_onhltdetamindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdetamindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdetamindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdetamindR_L1_1[h],"Pass L1_{1} ("+str(int(hists_onhltdetamindR_L1_1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdetamindR_HLT_1[h],"Pass HLT_{1} ("+str(int(hists_onhltdetamindR_HLT_1[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"detamindRtrg1.png")
            canvas.Close()

        hists_onhltdetamindR = [hist_onhltptdetamindR, hist_onhltetadetamindR]
        hists_onhltdetamindR_L1_2 = [hist_onhltptdetamindR_L1_2, hist_onhltetadetamindR_L1_2]
        hists_onhltdetamindR_HLT_2 = [hist_onhltptdetamindR_HLT_2, hist_onhltetadetamindR_HLT_2]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdetamindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdetamindR[h].Draw()
            hists_onhltdetamindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltdetamindR[h].SetLineWidth(3)
            hists_onhltdetamindR_L1_2[h].Draw("same")
            hists_onhltdetamindR_L1_2[h].SetLineColor(ROOT.kBlue)
            hists_onhltdetamindR_L1_2[h].SetLineWidth(2)
            hists_onhltdetamindR_HLT_2[h].Draw("same")
            hists_onhltdetamindR_HLT_2[h].SetLineColor(ROOT.kRed)
            hists_onhltdetamindR_HLT_2[h].SetLineWidth(1)
            hists_onhltdetamindR[h].SetTitle(";deta;Online deta(min dR)")
            hists_onhltdetamindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdetamindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdetamindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdetamindR_L1_2[h],"Pass L1_{2} ("+str(int(hists_onhltdetamindR_L1_2[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdetamindR_HLT_2[h],"Pass HLT_{2} ("+str(int(hists_onhltdetamindR_HLT_2[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"detamindRtrg2.png")
            canvas.Close()

        hists_onhltdetamindR = [hist_onhltptdetamindR, hist_onhltetadetamindR]
        hists_onhltdetamindR_L1 = [hist_onhltptdetamindR_L1, hist_onhltetadetamindR_L1]
        hists_onhltdetamindR_HLT = [hist_onhltptdetamindR_HLT, hist_onhltetadetamindR_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltdetamindR)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltdetamindR[h].Draw()
            hists_onhltdetamindR[h].SetLineColor(ROOT.kBlack)
            hists_onhltdetamindR[h].SetLineWidth(3)
            hists_onhltdetamindR_L1[h].Draw("same")
            hists_onhltdetamindR_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltdetamindR_L1[h].SetLineWidth(2)
            hists_onhltdetamindR_HLT[h].Draw("same")
            hists_onhltdetamindR_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltdetamindR_HLT[h].SetLineWidth(1)
            hists_onhltdetamindR[h].SetTitle(";deta;Online deta(min dR)")
            hists_onhltdetamindR[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltdetamindR[h],"Tau "+diff[h]+" ("+str(int(hists_onhltdetamindR[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdetamindR_L1[h],"Pass L1 ("+str(int(hists_onhltdetamindR_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltdetamindR_HLT[h],"Pass HLT ("+str(int(hists_onhltdetamindR_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"detamindR.png")
            canvas.Close()

        hists_onhltM = [hist_onhltptM, hist_onhltetaM]
        hists_onhltM_L1 = [hist_onhltptM_L1, hist_onhltetaM_L1]
        hists_onhltM_HLT = [hist_onhltptM_HLT, hist_onhltetaM_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltM)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltM[h].Draw()
            hists_onhltM[h].SetLineColor(ROOT.kBlack)
            hists_onhltM[h].SetLineWidth(3)
            hists_onhltM_L1[h].Draw("same")
            hists_onhltM_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltM_L1[h].SetLineWidth(2)
            hists_onhltM_HLT[h].Draw("same")
            hists_onhltM_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltM_HLT[h].SetLineWidth(1)
            hists_onhltM[h].SetTitle(";RNN M;n#circ Online #tau")
            hists_onhltM[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltM[h].SetMinimum(0.1)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            l_y_min = l_y_min_4-down
            l_y_max = l_y_max_U-down
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltM[h],"Tau "+diff[h]+" ("+str(int(hists_onhltM[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltM_L1[h],"Pass L1 ("+str(int(hists_onhltM_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltM_HLT[h],"Pass HLT ("+str(int(hists_onhltM_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"M.png")
            canvas.Close()

        hists_onhltMf = [hist_onhltptMf, hist_onhltetaMf]
        hists_onhltMf_L1 = [hist_onhltptMf_L1, hist_onhltetaMf_L1]
        hists_onhltMf_HLT = [hist_onhltptMf_HLT, hist_onhltetaMf_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltMf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onhltMf[h].Draw()
            hists_onhltMf[h].SetLineColor(ROOT.kBlack)
            hists_onhltMf[h].SetLineWidth(3)
            hists_onhltMf_L1[h].Draw("same")
            hists_onhltMf_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltMf_L1[h].SetLineWidth(2)
            hists_onhltMf_HLT[h].Draw("same")
            hists_onhltMf_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltMf_HLT[h].SetLineWidth(1)
            hists_onhltMf[h].SetTitle(";RNN M (only failed);n#circ Online #tau")
            hists_onhltMf[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhltMf[h].SetMinimum(0)
            if taus[t] == "passfail":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
            if taus[t] == "pass":
                l_x_min = l_x_min_L
                l_x_max = l_x_max_L
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltMf[h],"Tau "+diff[h]+" ("+str(int(hists_onhltMf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltMf_L1[h],"Pass L1 ("+str(int(hists_onhltMf_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltMf_HLT[h],"Pass HLT ("+str(int(hists_onhltMf_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"Mf.png")
            canvas.Close()

        hists_onhltnM = [hist_onhltptnM, hist_onhltetanM]
        hists_onhltnM_L1 = [hist_onhltptnM_L1, hist_onhltetanM_L1]
        hists_onhltnM_HLT = [hist_onhltptnM_HLT, hist_onhltetanM_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnM)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltnM[h].Draw()
            hists_onhltnM[h].SetLineColor(ROOT.kBlack)
            hists_onhltnM[h].SetLineWidth(3)
            hists_onhltnM_L1[h].Draw("same")
            hists_onhltnM_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltnM_L1[h].SetLineWidth(2)
            hists_onhltnM_HLT[h].Draw("same")
            hists_onhltnM_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltnM_HLT[h].SetLineWidth(1)
            hists_onhltnM[h].SetTitle(";n#circ Online #tau/event;Pass RNN M")
            hists_onhltnM[h].GetYaxis().SetTitleOffset(1.05)
            #hists_onhltnM[h].SetMinimum(0)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnM[h],"Tau "+diff[h]+" ("+str(int(hists_onhltnM[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltnM_L1[h],"Pass L1 ("+str(int(hists_onhltnM_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltnM_HLT[h],"Pass HLT ("+str(int(hists_onhltnM_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nM.png")
            canvas.Close()

        hists_onhltnMf = [hist_onhltptnMf, hist_onhltetanMf]
        hists_onhltnMf_L1 = [hist_onhltptnMf_L1, hist_onhltetanMf_L1]
        hists_onhltnMf_HLT = [hist_onhltptnMf_HLT, hist_onhltetanMf_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnMf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltnMf[h].Draw()
            hists_onhltnMf[h].SetLineColor(ROOT.kBlack)
            hists_onhltnMf[h].SetLineWidth(3)
            hists_onhltnMf_L1[h].Draw("same")
            hists_onhltnMf_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltnMf_L1[h].SetLineWidth(2)
            hists_onhltnMf_HLT[h].Draw("same")
            hists_onhltnMf_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltnMf_HLT[h].SetLineWidth(1)
            hists_onhltnMf[h].SetTitle(";n#circ Online #tau/event; Fail RNN M")
            hists_onhltnMf[h].GetYaxis().SetTitleOffset(1.05)
            #hists_onhltnMf[h].SetMinimum(0)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnMf[h],"Tau "+diff[h]+" ("+str(int(hists_onhltnMf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltnMf_L1[h],"Pass L1 ("+str(int(hists_onhltnMf_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltnMf_HLT[h],"Pass HLT ("+str(int(hists_onhltnMf_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nMf.png")
            canvas.Close()

        hists_onhltnMvsf = [hist_onhltptnMvsf, hist_onhltetanMvsf]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnMvsf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogz()
            hists_onhltnMvsf[h].Draw("COLZ")
            hists_onhltnMvsf[h].SetTitle(";n#circ Online #tau/event fail RNN M;n#circ Online #tau/event pass RNN M")
            hists_onhltnMvsf[h].GetYaxis().SetTitleOffset(0.95)
            hists_onhltnMvsf[h].SetNdivisions(5,"XY")
            l_x_min = l_x_min_R-0.15
            l_x_max = l_x_max_R-0.12
            legend = ROOT.TLegend(l_x_min, l_y_min_2, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnMvsf[h],"Tau "+diff[h]+" ("+str(int(hists_onhltnMvsf[h].GetEntries()))+")","")
            legend.Draw("same")
            canvas.SetRightMargin(0.15)
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nMvsf.png")
            canvas.Close()

        hists_onhltnMvsf_L1 = [hist_onhltptnMvsf_L1, hist_onhltetanMvsf_L1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnMvsf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogz()
            hists_onhltnMvsf_L1[h].Draw("COLZ")
            hists_onhltnMvsf_L1[h].SetTitle(";n#circ Online #tau/event fail RNN M;n#circ Online #tau/event pass RNN M")
            hists_onhltnMvsf_L1[h].GetYaxis().SetTitleOffset(0.95)
            hists_onhltnMvsf_L1[h].SetNdivisions(5,"XY")
            l_x_min = l_x_min_R-0.15
            l_x_max = l_x_max_R-0.12
            legend = ROOT.TLegend(l_x_min, l_y_min_2, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnMvsf_L1[h],"Tau "+diff[h]+" L1 ("+str(int(hists_onhltnMvsf_L1[h].GetEntries()))+")","")
            legend.Draw("same")
            canvas.SetRightMargin(0.15)
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nMvsfL1.png")
            canvas.Close()

        hists_onhltnMvsf_HLT = [hist_onhltptnMvsf_HLT, hist_onhltetanMvsf_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnMvsf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogz()
            hists_onhltnMvsf_HLT[h].Draw("COLZ")
            hists_onhltnMvsf_HLT[h].SetTitle(";n#circ Online #tau/event fail RNN M;n#circ Online #tau/event pass RNN M")
            hists_onhltnMvsf_HLT[h].GetYaxis().SetTitleOffset(0.95)
            hists_onhltnMvsf_HLT[h].SetNdivisions(5,"XY")
            l_x_min = l_x_min_R-0.15
            l_x_max = l_x_max_R-0.12
            legend = ROOT.TLegend(l_x_min, l_y_min_2, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnMvsf_HLT[h],"Tau "+diff[h]+" HLT ("+str(int(hists_onhltnMvsf_HLT[h].GetEntries()))+")","")
            legend.Draw("same")
            canvas.SetRightMargin(0.15)
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nMvsfHLT.png")
            canvas.Close()

        hists_onhltnCvsf = [hist_onhltptnCvsf, hist_onhltetanCvsf]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnCvsf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogz()
            hists_onhltnCvsf[h].Draw("COLZ")
            hists_onhltnCvsf[h].SetTitle(";n#circ Online #tau/event fail Custom cuts;n#circ Online #tau/event pass Custom cuts")
            hists_onhltnCvsf[h].GetYaxis().SetTitleOffset(0.95)
            hists_onhltnCvsf[h].SetNdivisions(5,"XY")
            l_x_min = l_x_min_R-0.15
            l_x_max = l_x_max_R-0.12
            legend = ROOT.TLegend(l_x_min, l_y_min_2, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnCvsf[h],"Tau "+diff[h]+" ("+str(int(hists_onhltCvsf[h].GetEntries()))+")","")
            legend.Draw("same")
            canvas.SetRightMargin(0.15)
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nCvsf.png")
            canvas.Close()

        hists_onhltnCvsf_L1 = [hist_onhltptnCvsf_L1, hist_onhltetanCvsf_L1]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnCvsf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogz()
            hists_onhltnCvsf_L1[h].Draw("COLZ")
            hists_onhltnCvsf_L1[h].SetTitle(";n#circ Online #tau/event fail Custom cuts;n#circ Online #tau/event pass Custom cuts")
            hists_onhltnCvsf_L1[h].GetYaxis().SetTitleOffset(0.95)
            hists_onhltnCvsf_L1[h].SetNdivisions(5,"XY")
            l_x_min = l_x_min_R-0.15
            l_x_max = l_x_max_R-0.12
            legend = ROOT.TLegend(l_x_min, l_y_min_2, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnCvsf_L1[h],"Tau "+diff[h]+" L1 ("+str(int(hists_onhltnCvsf_L1[h].GetEntries()))+")","")
            legend.Draw("same")
            canvas.SetRightMargin(0.15)
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nCvsfL1.png")
            canvas.Close()

        hists_onhltnCvsf_HLT = [hist_onhltptnCvsf_HLT, hist_onhltetanCvsf_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltnCvsf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogz()
            hists_onhltnCvsf_HLT[h].Draw("COLZ")
            hists_onhltnCvsf_HLT[h].SetTitle(";n#circ Online #tau/event fail Custom cuts;n#circ Online #tau/event pass Custom cuts")
            hists_onhltnCvsf_HLT[h].GetYaxis().SetTitleOffset(0.95)
            hists_onhltnCvsf_HLT[h].SetNdivisions(5,"XY")
            l_x_min = l_x_min_R-0.15
            l_x_max = l_x_max_R-0.12
            legend = ROOT.TLegend(l_x_min, l_y_min_2, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltnCvsf_HLT[h],"Tau "+diff[h]+" HLT ("+str(int(hists_onhltnCvsf_HLT[h].GetEntries()))+")","")
            legend.Draw("same")
            canvas.SetRightMargin(0.15)
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"nCvsfHLT.png")
            canvas.Close()

        hists_onhltndRf = [hist_onhltptndRf, hist_onhltetandRf]
        hists_onhltndRf_L1 = [hist_onhltptndRf_L1, hist_onhltetandRf_L1]
        hists_onhltndRf_HLT = [hist_onhltptndRf_HLT, hist_onhltetandRf_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltndRf)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltndRf[h].Draw()
            hists_onhltndRf[h].SetLineColor(ROOT.kBlack)
            hists_onhltndRf[h].SetLineWidth(3)
            hists_onhltndRf_L1[h].Draw("same")
            hists_onhltndRf_L1[h].SetLineColor(ROOT.kBlue)
            hists_onhltndRf_L1[h].SetLineWidth(2)
            hists_onhltndRf_HLT[h].Draw("same")
            hists_onhltndRf_HLT[h].SetLineColor(ROOT.kRed)
            hists_onhltndRf_HLT[h].SetLineWidth(1)
            hists_onhltndRf[h].SetTitle(";n#circ Online #tau/event;Fail dR cut")
            hists_onhltndRf[h].GetYaxis().SetTitleOffset(1.05)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_4, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltndRf[h],"Tau "+diff[h]+" ("+str(int(hists_onhltndRf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltndRf_L1[h],"Pass L1 ("+str(int(hists_onhltndRf_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltndRf_HLT[h],"Pass HLT ("+str(int(hists_onhltndRf_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"ndRf.png")
            canvas.Close()

        hists_onMhltdR01 = [hist_onMhltptdR01, hist_onMhltetadR01]
        hists_onMhltdR01_L1 = [hist_onMhltptdR01_L1, hist_onMhltetadR01_L1]
        hists_onMhltdR01_HLT = [hist_onMhltptdR01_HLT, hist_onMhltetadR01_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onMhltdR01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onMhltdR01[h].Draw()
            hists_onMhltdR01[h].SetLineColor(ROOT.kBlack)
            hists_onMhltdR01[h].SetLineWidth(3)
            hists_onMhltdR01_L1[h].Draw("same")
            hists_onMhltdR01_L1[h].SetLineColor(ROOT.kBlue)
            hists_onMhltdR01_L1[h].SetLineWidth(2)
            hists_onMhltdR01_HLT[h].Draw("same")
            hists_onMhltdR01_HLT[h].SetLineColor(ROOT.kRed)
            hists_onMhltdR01_HLT[h].SetLineWidth(1)
            hists_onMhltdR01[h].SetTitle(";dR;dR(lead#tau,subl#tau)")
            hists_onMhltdR01[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onMhltdR01[h],"Tau M "+diff[h]+" ("+str(int(hists_onMhltdR01[h].GetEntries()))+")")
            legend.AddEntry(hists_onMhltdR01_L1[h],"Pass L1 ("+str(int(hists_onMhltdR01_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onMhltdR01_HLT[h],"Pass HLT ("+str(int(hists_onMhltdR01_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onM"+diff[h]+"dR01.png")
            canvas.Close()

        hists_onMhltdphi01 = [hist_onMhltptdphi01, hist_onMhltetadphi01]
        hists_onMhltdphi01_L1 = [hist_onMhltptdphi01_L1, hist_onMhltetadphi01_L1]
        hists_onMhltdphi01_HLT = [hist_onMhltptdphi01_HLT, hist_onMhltetadphi01_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onMhltdphi01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onMhltdphi01[h].Draw()
            hists_onMhltdphi01[h].SetLineColor(ROOT.kBlack)
            hists_onMhltdphi01[h].SetLineWidth(3)
            hists_onMhltdphi01_L1[h].Draw("same")
            hists_onMhltdphi01_L1[h].SetLineColor(ROOT.kBlue)
            hists_onMhltdphi01_L1[h].SetLineWidth(2)
            hists_onMhltdphi01_HLT[h].Draw("same")
            hists_onMhltdphi01_HLT[h].SetLineColor(ROOT.kRed)
            hists_onMhltdphi01_HLT[h].SetLineWidth(1)
            hists_onMhltdphi01[h].SetTitle(";|dphi|;|dphi(lead#tau,subl#tau)|")
            hists_onMhltdphi01[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onMhltdphi01[h],"Tau M "+diff[h]+" ("+str(int(hists_onMhltdphi01[h].GetEntries()))+")")
            legend.AddEntry(hists_onMhltdphi01_L1[h],"Pass L1 ("+str(int(hists_onMhltdphi01_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onMhltdphi01_HLT[h],"Pass HLT ("+str(int(hists_onMhltdphi01_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onM"+diff[h]+"dphi01.png")
            canvas.Close()

        hists_onMhltdeta01 = [hist_onMhltptdeta01, hist_onMhltetadeta01]
        hists_onMhltdeta01_L1 = [hist_onMhltptdeta01_L1, hist_onMhltetadeta01_L1]
        hists_onMhltdeta01_HLT = [hist_onMhltptdeta01_HLT, hist_onMhltetadeta01_HLT]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onMhltdeta01)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy(0)
            hists_onMhltdeta01[h].Draw()
            hists_onMhltdeta01[h].SetLineColor(ROOT.kBlack)
            hists_onMhltdeta01[h].SetLineWidth(3)
            hists_onMhltdeta01_L1[h].Draw("same")
            hists_onMhltdeta01_L1[h].SetLineColor(ROOT.kBlue)
            hists_onMhltdeta01_L1[h].SetLineWidth(2)
            hists_onMhltdeta01_HLT[h].Draw("same")
            hists_onMhltdeta01_HLT[h].SetLineColor(ROOT.kRed)
            hists_onMhltdeta01_HLT[h].SetLineWidth(1)
            hists_onMhltdeta01[h].SetTitle(";deta;deta(lead#tau,subl#tau)")
            hists_onMhltdeta01[h].GetYaxis().SetTitleOffset(1.05)
            legend = ROOT.TLegend(0.675,0.75,0.95,0.95)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onMhltdeta01[h],"Tau M "+diff[h]+" ("+str(int(hists_onMhltdeta01[h].GetEntries()))+")")
            legend.AddEntry(hists_onMhltdeta01_L1[h],"Pass L1 ("+str(int(hists_onMhltdeta01_L1[h].GetEntries()))+")")
            legend.AddEntry(hists_onMhltdeta01_HLT[h],"Pass HLT ("+str(int(hists_onMhltdeta01_HLT[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"onM"+diff[h]+"deta01.png")
            canvas.Close()

        hists_onhltpt = [hist_onhltptpt, hist_onhltetapt]
        hists_onhltpt_VL = [hist_onhltptpt_VL, hist_onhltetapt_VL]
        hists_onhltpt_L = [hist_onhltptpt_L, hist_onhltetapt_L]
        hists_onhltpt_M = [hist_onhltptpt_M, hist_onhltetapt_M]
        hists_onhltpt_T = [hist_onhltptpt_T, hist_onhltetapt_T]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltpt[h].Draw()
            hists_onhltpt[h].SetLineColor(ROOT.kBlack)
            hists_onhltpt[h].SetLineWidth(5)
            hists_onhltpt_VL[h].Draw("same")
            hists_onhltpt_VL[h].SetLineColor(ROOT.kBlue)
            hists_onhltpt_VL[h].SetLineWidth(4)
            hists_onhltpt_L[h].Draw("same")
            hists_onhltpt_L[h].SetLineColor(ROOT.kGreen)
            hists_onhltpt_L[h].SetLineWidth(3)
            hists_onhltpt_M[h].Draw("same")
            hists_onhltpt_M[h].SetLineColor(ROOT.kOrange)
            hists_onhltpt_M[h].SetLineWidth(2)
            hists_onhltpt_T[h].Draw("same")
            hists_onhltpt_T[h].SetLineColor(ROOT.kRed)
            hists_onhltpt_T[h].SetLineWidth(1)
            hists_onhltpt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltpt[h].SetAxisRange(0,800,"X")
            hists_onhltpt[h].GetYaxis().SetTitleOffset(1.05)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_6, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltpt[h],"Tau "+diff[h]+" ("+str(int(hists_onhltpt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_VL[h],"RNN VL ("+str(int(hists_onhltpt_VL[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_L[h],"RNN L ("+str(int(hists_onhltpt_L[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_M[h],"RNN M ("+str(int(hists_onhltpt_M[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_T[h],"RNN T ("+str(int(hists_onhltpt_T[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"ptRNNID.png")
            canvas.Close()
        '''
        #THStack stack_onhltpt("stack_onhltpt","")
        hist_onhltptpt_TEST = hist_onhltptpt.Clone()
        hist_onhltetapt_TEST = hist_onhltetapt.Clone()
        hist_onhltptpt_VL_TEST = hist_onhltptpt_VL.Clone()
        hist_onhltetapt_VL_TEST = hist_onhltetapt_VL.Clone()
        hist_onhltptpt_L_TEST = hist_onhltptpt_L.Clone()
        hist_onhltetapt_L_TEST = hist_onhltetapt_L.Clone()
        hist_onhltptpt_M_TEST = hist_onhltptpt_M.Clone()
        hist_onhltetapt_M_TEST = hist_onhltetapt_M.Clone()
        hist_onhltptpt_T_TEST = hist_onhltptpt_T.Clone()
        hist_onhltetapt_T_TEST = hist_onhltetapt_T.Clone()

        hists_onhltpt_TEST = [hist_onhltptpt_TEST, hist_onhltetapt_TEST]
        hists_onhltpt_VL_TEST = [hist_onhltptpt_VL_TEST, hist_onhltetapt_VL_TEST]
        hists_onhltpt_L_TEST = [hist_onhltptpt_L_TEST, hist_onhltetapt_L_TEST]
        hists_onhltpt_M_TEST = [hist_onhltptpt_M_TEST, hist_onhltetapt_M_TEST]
        hists_onhltpt_T_TEST = [hist_onhltptpt_T_TEST, hist_onhltetapt_T_TEST]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltpt_TEST[h].Draw()
            hists_onhltpt_TEST[h].SetLineWidth(1)
            hists_onhltpt_TEST[h].SetFillColorAlpha(ROOT.kBlack,0.7)
            hists_onhltpt_VL_TEST[h].Draw("same")
            hists_onhltpt_VL_TEST[h].SetLineWidth(1)
            hists_onhltpt_VL_TEST[h].SetFillColorAlpha(ROOT.kBlue,0.7)
            hists_onhltpt_L_TEST[h].Draw("same")
            hists_onhltpt_L_TEST[h].SetLineWidth(1)
            hists_onhltpt_L_TEST[h].SetFillColorAlpha(ROOT.kGreen,0.7)
            hists_onhltpt_M_TEST[h].Draw("same")
            hists_onhltpt_M_TEST[h].SetLineWidth(1)
            hists_onhltpt_M_TEST[h].SetFillColorAlpha(ROOT.kOrange,0.7)
            hists_onhltpt_T_TEST[h].Draw("same")
            hists_onhltpt_T_TEST[h].SetLineWidth(1)
            hists_onhltpt_T_TEST[h].SetFillColorAlpha(ROOT.kRed,0.7)
            hists_onhltpt_TEST[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltpt_TEST[h].SetAxisRange(0,800,"X")
            hists_onhltpt_TEST[h].GetYaxis().SetTitleOffset(1.05)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            legend = ROOT.TLegend(l_x_min, l_y_min_6, l_x_max, l_y_max_U)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltpt_TEST[h],"Tau "+diff[h]+" ("+str(int(hists_onhltpt_TEST[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_VL_TEST[h],"RNN VL ("+str(int(hists_onhltpt_VL_TEST[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_L_TEST[h],"RNN L ("+str(int(hists_onhltpt_L_TEST[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_M_TEST[h],"RNN M ("+str(int(hists_onhltpt_M_TEST[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_T_TEST[h],"RNN T ("+str(int(hists_onhltpt_T_TEST[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"ptRNNIDTEST.png")
            canvas.Close()
        '''
        hists_onhlteta = [hist_onhltpteta, hist_onhltetaeta]
        hists_onhlteta_VL = [hist_onhltpteta_VL, hist_onhltetaeta_VL]
        hists_onhlteta_L = [hist_onhltpteta_L, hist_onhltetaeta_L]
        hists_onhlteta_M = [hist_onhltpteta_M, hist_onhltetaeta_M]
        hists_onhlteta_T = [hist_onhltpteta_T, hist_onhltetaeta_T]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhlteta)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhlteta[h].Draw()
            hists_onhlteta[h].SetLineColor(ROOT.kBlack)
            hists_onhlteta[h].SetLineWidth(5)
            hists_onhlteta_VL[h].Draw("same")
            hists_onhlteta_VL[h].SetLineColor(ROOT.kBlue)
            hists_onhlteta_VL[h].SetLineWidth(4)
            hists_onhlteta_L[h].Draw("same")
            hists_onhlteta_L[h].SetLineColor(ROOT.kGreen)
            hists_onhlteta_L[h].SetLineWidth(3)
            hists_onhlteta_M[h].Draw("same")
            hists_onhlteta_M[h].SetLineColor(ROOT.kOrange)
            hists_onhlteta_M[h].SetLineWidth(2)
            hists_onhlteta_T[h].Draw("same")
            hists_onhlteta_T[h].SetLineColor(ROOT.kRed)
            hists_onhlteta_T[h].SetLineWidth(1)
            hists_onhlteta[h].SetTitle(";eta^{#tau};Online eta^{#tau}")
            hists_onhlteta[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhlteta[h].SetMinimum(0.1)
            if taus[t] == "passfail":
                l_x_min = l_x_min_C
                l_x_max = l_x_max_C
                l_y_min = l_y_min_6-down
                l_y_max = l_y_max_U-down
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
                l_y_min = l_y_min_6
                l_y_max = l_y_max_U
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhlteta[h],"Tau "+diff[h]+" ("+str(int(hists_onhlteta[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_VL[h],"RNN VL ("+str(int(hists_onhlteta_VL[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_L[h],"RNN L ("+str(int(hists_onhlteta_L[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_M[h],"RNN M ("+str(int(hists_onhlteta_M[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_T[h],"RNN T ("+str(int(hists_onhlteta_T[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"etaRNNID.png")
            canvas.Close()

        hists_onhltRNNScore = [hist_onhltptRNNScore, hist_onhltetaRNNScore]
        hists_onhltRNNScore_VL = [hist_onhltptRNNScore_VL, hist_onhltetaRNNScore_VL]
        hists_onhltRNNScore_L = [hist_onhltptRNNScore_L, hist_onhltetaRNNScore_L]
        hists_onhltRNNScore_M = [hist_onhltptRNNScore_M, hist_onhltetaRNNScore_M]
        hists_onhltRNNScore_T = [hist_onhltptRNNScore_T, hist_onhltetaRNNScore_T]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltRNNScore)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltRNNScore[h].Draw()
            hists_onhltRNNScore[h].SetLineColor(ROOT.kBlack)
            hists_onhltRNNScore[h].SetLineWidth(5)
            hists_onhltRNNScore_VL[h].Draw("same")
            hists_onhltRNNScore_VL[h].SetLineColor(ROOT.kBlue)
            hists_onhltRNNScore_VL[h].SetLineWidth(4)
            hists_onhltRNNScore_L[h].Draw("same")
            hists_onhltRNNScore_L[h].SetLineColor(ROOT.kGreen)
            hists_onhltRNNScore_L[h].SetLineWidth(3)
            hists_onhltRNNScore_M[h].Draw("same")
            hists_onhltRNNScore_M[h].SetLineColor(ROOT.kOrange)
            hists_onhltRNNScore_M[h].SetLineWidth(2)
            hists_onhltRNNScore_T[h].Draw("same")
            hists_onhltRNNScore_T[h].SetLineColor(ROOT.kRed)
            hists_onhltRNNScore_T[h].SetLineWidth(1)
            hists_onhltRNNScore[h].SetTitle(";RNN Score;Online #tau RNN Score")
            hists_onhltRNNScore[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
                l_y_min = l_y_min_6
                l_y_max = l_y_max_U
            if taus[t] == "pass":
                l_x_min = l_x_min_C
                l_x_max = l_x_max_C
                l_y_min = l_y_min_6-down
                l_y_max = l_y_max_U-down
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltRNNScore[h],"Tau "+diff[h]+" ("+str(int(hists_onhltRNNScore[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_VL[h],"RNN VL ("+str(int(hists_onhltRNNScore_VL[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_L[h],"RNN L ("+str(int(hists_onhltRNNScore_L[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_M[h],"RNN M ("+str(int(hists_onhltRNNScore_M[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_T[h],"RNN T ("+str(int(hists_onhltRNNScore_T[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"RNNScoreRNNID.png")
            canvas.Close()

        hists_onhltpt = [hist_onhltptpt, hist_onhltetapt]
        hists_onhltpt_Tf = [hist_onhltptpt_Tf, hist_onhltetapt_Tf]
        hists_onhltpt_Mf = [hist_onhltptpt_Mf, hist_onhltetapt_Mf]
        hists_onhltpt_Lf = [hist_onhltptpt_Lf, hist_onhltetapt_Lf]
        hists_onhltpt_VLf = [hist_onhltptpt_VLf, hist_onhltetapt_VLf]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltpt[h].Draw()
            hists_onhltpt[h].SetLineColor(ROOT.kBlack)
            hists_onhltpt[h].SetLineWidth(5)
            hists_onhltpt_Tf[h].Draw("same")
            hists_onhltpt_Tf[h].SetLineColor(ROOT.kRed)
            hists_onhltpt_Tf[h].SetLineWidth(4)
            hists_onhltpt_Mf[h].Draw("same")
            hists_onhltpt_Mf[h].SetLineColor(ROOT.kOrange)
            hists_onhltpt_Mf[h].SetLineWidth(3)
            hists_onhltpt_Lf[h].Draw("same")
            hists_onhltpt_Lf[h].SetLineColor(ROOT.kGreen)
            hists_onhltpt_Lf[h].SetLineWidth(2)
            hists_onhltpt_VLf[h].Draw("same")
            hists_onhltpt_VLf[h].SetLineColor(ROOT.kBlue)
            hists_onhltpt_VLf[h].SetLineWidth(1)
            hists_onhltpt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltpt[h].SetAxisRange(0,800,"X")
            hists_onhltpt[h].GetYaxis().SetTitleOffset(1.05)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            l_y_min = l_y_min_6
            l_y_max = l_y_max_U
            legend = ROOT.TLegend(l_x_min, l_y_min_6, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltpt[h],"Tau "+diff[h]+" ("+str(int(hists_onhltpt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_Tf[h],"Not RNN T ("+str(int(hists_onhltpt_Tf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_Mf[h],"Not RNN M ("+str(int(hists_onhltpt_Mf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_Lf[h],"Not RNN L ("+str(int(hists_onhltpt_Lf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_VLf[h],"Not RNN VL ("+str(int(hists_onhltpt_VLf[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"ptRNNIDf.png")
            canvas.Close()

        hists_onhltpt = [hist_onhltptpt, hist_onhltetapt]
        hists_onhltpt_Cf = [hist_onhltptpt_Cf, hist_onhltetapt_Cf]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltpt)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltpt[h].Draw()
            hists_onhltpt[h].SetLineColor(ROOT.kBlack)
            hists_onhltpt[h].SetLineWidth(2)
            hists_onhltpt_Cf[h].Draw("same")
            hists_onhltpt_Cf[h].SetLineColor(ROOT.kRed)
            hists_onhltpt_Cf[h].SetLineWidth(1)
            hists_onhltpt[h].SetTitle(";p^{#tau}_{T} (GeV);Online p^{"+diff[h]+"#tau}_{T}")
            hists_onhltpt[h].SetAxisRange(0,800,"X")
            hists_onhltpt[h].GetYaxis().SetTitleOffset(1.05)
            l_x_min = l_x_min_R
            l_x_max = l_x_max_R
            l_y_min = l_y_min_3
            l_y_max = l_y_max_U
            legend = ROOT.TLegend(l_x_min, l_y_min_3, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltpt[h],"Tau "+diff[h]+" ("+str(int(hists_onhltpt[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltpt_Cf[h],"Not CC ("+str(int(hists_onhltpt_Cf[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"ptCf.png")
            canvas.Close()

        hists_onhlteta = [hist_onhltpteta, hist_onhltetaeta]
        hists_onhlteta_Tf = [hist_onhltpteta_Tf, hist_onhltetaeta_Tf]
        hists_onhlteta_Mf = [hist_onhltpteta_Mf, hist_onhltetaeta_Mf]
        hists_onhlteta_Lf = [hist_onhltpteta_Lf, hist_onhltetaeta_Lf]
        hists_onhlteta_VLf = [hist_onhltpteta_VLf, hist_onhltetaeta_VLf]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhlteta)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhlteta[h].Draw()
            hists_onhlteta[h].SetLineColor(ROOT.kBlack)
            hists_onhlteta[h].SetLineWidth(5)
            hists_onhlteta_Tf[h].Draw("same")
            hists_onhlteta_Tf[h].SetLineColor(ROOT.kRed)
            hists_onhlteta_Tf[h].SetLineWidth(4)
            hists_onhlteta_Mf[h].Draw("same")
            hists_onhlteta_Mf[h].SetLineColor(ROOT.kOrange)
            hists_onhlteta_Mf[h].SetLineWidth(3)
            hists_onhlteta_Lf[h].Draw("same")
            hists_onhlteta_Lf[h].SetLineColor(ROOT.kGreen)
            hists_onhlteta_Lf[h].SetLineWidth(2)
            hists_onhlteta_VLf[h].Draw("same")
            hists_onhlteta_VLf[h].SetLineColor(ROOT.kBlue)
            hists_onhlteta_VLf[h].SetLineWidth(1)
            hists_onhlteta[h].SetTitle(";eta^{#tau};Online eta^{#tau}")
            hists_onhlteta[h].GetYaxis().SetTitleOffset(1.05)
            hists_onhlteta[h].SetMinimum(0.1)
            if taus[t] == "passfail":
                l_x_min = l_x_min_C
                l_x_max = l_x_max_C
                l_y_min = l_y_min_6-down
                l_y_max = l_y_max_U-down
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
                l_y_min = l_y_min_6
                l_y_max = l_y_max_U
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhlteta[h],"Tau "+diff[h]+" ("+str(int(hists_onhlteta[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_Tf[h],"Not RNN T ("+str(int(hists_onhlteta_Tf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_Mf[h],"Not RNN M ("+str(int(hists_onhlteta_Mf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_Lf[h],"Not RNN L ("+str(int(hists_onhlteta_Lf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhlteta_VLf[h],"Not RNN VL ("+str(int(hists_onhlteta_VLf[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"etaRNNIDf.png")
            canvas.Close()

        hists_onhltRNNScore = [hist_onhltptRNNScore, hist_onhltetaRNNScore]
        hists_onhltRNNScore_Tf = [hist_onhltptRNNScore_Tf, hist_onhltetaRNNScore_Tf]
        hists_onhltRNNScore_Mf = [hist_onhltptRNNScore_Mf, hist_onhltetaRNNScore_Mf]
        hists_onhltRNNScore_Lf = [hist_onhltptRNNScore_Lf, hist_onhltetaRNNScore_Lf]
        hists_onhltRNNScore_VLf = [hist_onhltptRNNScore_VLf, hist_onhltetaRNNScore_VLf]
        diff = ["hltpt", "hlteta"]
        for h in range(len(hists_onhltRNNScore)):
            canvas = ROOT.TCanvas("c")
            canvas.cd()
            canvas.SetLogy()
            hists_onhltRNNScore[h].Draw()
            hists_onhltRNNScore[h].SetLineColor(ROOT.kBlack)
            hists_onhltRNNScore[h].SetLineWidth(5)
            hists_onhltRNNScore_Tf[h].Draw("same")
            hists_onhltRNNScore_Tf[h].SetLineColor(ROOT.kRed)
            hists_onhltRNNScore_Tf[h].SetLineWidth(4)
            hists_onhltRNNScore_Mf[h].Draw("same")
            hists_onhltRNNScore_Mf[h].SetLineColor(ROOT.kOrange)
            hists_onhltRNNScore_Mf[h].SetLineWidth(3)
            hists_onhltRNNScore_Lf[h].Draw("same")
            hists_onhltRNNScore_Lf[h].SetLineColor(ROOT.kGreen)
            hists_onhltRNNScore_Lf[h].SetLineWidth(2)
            hists_onhltRNNScore_VLf[h].Draw("same")
            hists_onhltRNNScore_VLf[h].SetLineColor(ROOT.kBlue)
            hists_onhltRNNScore_VLf[h].SetLineWidth(1)
            hists_onhltRNNScore[h].SetTitle(";RNN Score;Online #tau RNN Score")
            hists_onhltRNNScore[h].GetYaxis().SetTitleOffset(1.05)
            if taus[t] == "passfail":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
                l_y_min = l_y_min_6
                l_y_max = l_y_max_U
            if taus[t] == "pass":
                l_x_min = l_x_min_R
                l_x_max = l_x_max_R
                l_y_min = l_y_min_6-down
                l_y_max = l_y_max_U-down
            legend = ROOT.TLegend(l_x_min, l_y_min, l_x_max, l_y_max)
            legend.SetTextSize(0.035)
            legend.SetBorderSize(1)
            legend.SetHeader("#kappa_{#lambda}="+str(kL[k]),"C")
            legend.AddEntry(hists_onhltRNNScore[h],"Tau "+diff[h]+" ("+str(int(hists_onhltRNNScore[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_Tf[h],"Not RNN T ("+str(int(hists_onhltRNNScore_Tf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_Mf[h],"Not RNN M ("+str(int(hists_onhltRNNScore_Mf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_Lf[h],"Not RNN L ("+str(int(hists_onhltRNNScore_Lf[h].GetEntries()))+")")
            legend.AddEntry(hists_onhltRNNScore_VLf[h],"Not RNN VL ("+str(int(hists_onhltRNNScore_VLf[h].GetEntries()))+")")
            legend.Draw("same")
            canvas.Update()
            canvas.Print(taus[t]+str(kL[k])+"on"+diff[h]+"RNNScoreRNNIDf.png")
            canvas.Close()

        #hist_onhltptpt_HLT.Delete()
        #hist_onhltpt0pt_HLT.Delete()
        #hist_onhltpt1pt_HLT.Delete()

// Author: Shiwen An
// Date: 2022.05.20
// Purpose:
// Comparison Plots for 
// Crosscheck 

//================Offline_Matched_Taus=====================
TH1F* Offline_Matched_Taus_Pt(){
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Sun May 22 21:28:32 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",1,1,4,4);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *PtoPcP__1 = new TH1F("PtoPcP__1","Offline_Matched_Taus.Pt()",100,0,790);
   PtoPcP__1->SetBinContent(2,1178);
   PtoPcP__1->SetBinContent(3,3793);
   PtoPcP__1->SetBinContent(4,4046);
   PtoPcP__1->SetBinContent(5,3774);
   PtoPcP__1->SetBinContent(6,3253);
   PtoPcP__1->SetBinContent(7,2956);
   PtoPcP__1->SetBinContent(8,2579);
   PtoPcP__1->SetBinContent(9,2270);
   PtoPcP__1->SetBinContent(10,1952);
   PtoPcP__1->SetBinContent(11,1743);
   PtoPcP__1->SetBinContent(12,1485);
   PtoPcP__1->SetBinContent(13,1232);
   PtoPcP__1->SetBinContent(14,1142);
   PtoPcP__1->SetBinContent(15,918);
   PtoPcP__1->SetBinContent(16,820);
   PtoPcP__1->SetBinContent(17,681);
   PtoPcP__1->SetBinContent(18,531);
   PtoPcP__1->SetBinContent(19,521);
   PtoPcP__1->SetBinContent(20,411);
   PtoPcP__1->SetBinContent(21,333);
   PtoPcP__1->SetBinContent(22,300);
   PtoPcP__1->SetBinContent(23,204);
   PtoPcP__1->SetBinContent(24,204);
   PtoPcP__1->SetBinContent(25,171);
   PtoPcP__1->SetBinContent(26,162);
   PtoPcP__1->SetBinContent(27,95);
   PtoPcP__1->SetBinContent(28,93);
   PtoPcP__1->SetBinContent(29,84);
   PtoPcP__1->SetBinContent(30,68);
   PtoPcP__1->SetBinContent(31,49);
   PtoPcP__1->SetBinContent(32,58);
   PtoPcP__1->SetBinContent(33,35);
   PtoPcP__1->SetBinContent(34,32);
   PtoPcP__1->SetBinContent(35,37);
   PtoPcP__1->SetBinContent(36,22);
   PtoPcP__1->SetBinContent(37,13);
   PtoPcP__1->SetBinContent(38,21);
   PtoPcP__1->SetBinContent(39,22);
   PtoPcP__1->SetBinContent(40,11);
   PtoPcP__1->SetBinContent(41,18);
   PtoPcP__1->SetBinContent(42,13);
   PtoPcP__1->SetBinContent(43,6);
   PtoPcP__1->SetBinContent(44,6);
   PtoPcP__1->SetBinContent(45,11);
   PtoPcP__1->SetBinContent(46,9);
   PtoPcP__1->SetBinContent(47,7);
   PtoPcP__1->SetBinContent(48,4);
   PtoPcP__1->SetBinContent(49,5);
   PtoPcP__1->SetBinContent(50,2);
   PtoPcP__1->SetBinContent(51,3);
   PtoPcP__1->SetBinContent(52,5);
   PtoPcP__1->SetBinContent(54,2);
   PtoPcP__1->SetBinContent(55,1);
   PtoPcP__1->SetBinContent(56,2);
   PtoPcP__1->SetBinContent(58,2);
   PtoPcP__1->SetBinContent(59,1);
   PtoPcP__1->SetBinContent(60,1);
   PtoPcP__1->SetBinContent(61,1);
   PtoPcP__1->SetBinContent(62,1);
   PtoPcP__1->SetBinContent(63,1);
   PtoPcP__1->SetBinContent(64,1);
   PtoPcP__1->SetBinContent(65,1);
   PtoPcP__1->SetBinContent(70,1);
   PtoPcP__1->SetBinContent(76,1);
   PtoPcP__1->SetBinContent(80,2);
   PtoPcP__1->SetBinContent(82,1);
   PtoPcP__1->SetBinContent(84,1);
   PtoPcP__1->SetBinContent(88,2);
   PtoPcP__1->SetBinContent(92,1);
   PtoPcP__1->SetEntries(37411);
   PtoPcP__1->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   PtoPcP__1->SetLineColor(ci);
   PtoPcP__1->GetXaxis()->SetRange(1,100);
   PtoPcP__1->GetXaxis()->SetLabelFont(42);
   PtoPcP__1->GetXaxis()->SetTitleOffset(1);
   PtoPcP__1->GetXaxis()->SetTitleFont(42);
   PtoPcP__1->GetYaxis()->SetLabelFont(42);
   PtoPcP__1->GetYaxis()->SetTitleFont(42);
   PtoPcP__1->GetZaxis()->SetLabelFont(42);
   PtoPcP__1->GetZaxis()->SetTitleOffset(1);
   PtoPcP__1->GetZaxis()->SetTitleFont(42);
   PtoPcP__1->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return PtoPcP__1;
}

TH1F* Offline_Matched_Taus_Eta(){
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Sun May 22 21:33:47 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *EtaoPcP__2 = new TH1F("EtaoPcP__2","Offline_Matched_Taus.Eta()",100,-3,3);
   EtaoPcP__2->SetBinContent(8,3);
   EtaoPcP__2->SetBinContent(9,51);
   EtaoPcP__2->SetBinContent(10,110);
   EtaoPcP__2->SetBinContent(11,122);
   EtaoPcP__2->SetBinContent(12,151);
   EtaoPcP__2->SetBinContent(13,153);
   EtaoPcP__2->SetBinContent(14,164);
   EtaoPcP__2->SetBinContent(15,169);
   EtaoPcP__2->SetBinContent(16,213);
   EtaoPcP__2->SetBinContent(17,195);
   EtaoPcP__2->SetBinContent(18,227);
   EtaoPcP__2->SetBinContent(19,250);
   EtaoPcP__2->SetBinContent(20,265);
   EtaoPcP__2->SetBinContent(21,293);
   EtaoPcP__2->SetBinContent(22,312);
   EtaoPcP__2->SetBinContent(23,324);
   EtaoPcP__2->SetBinContent(24,337);
   EtaoPcP__2->SetBinContent(25,351);
   EtaoPcP__2->SetBinContent(26,375);
   EtaoPcP__2->SetBinContent(27,419);
   EtaoPcP__2->SetBinContent(28,407);
   EtaoPcP__2->SetBinContent(29,471);
   EtaoPcP__2->SetBinContent(30,482);
   EtaoPcP__2->SetBinContent(31,480);
   EtaoPcP__2->SetBinContent(32,533);
   EtaoPcP__2->SetBinContent(33,510);
   EtaoPcP__2->SetBinContent(34,517);
   EtaoPcP__2->SetBinContent(35,568);
   EtaoPcP__2->SetBinContent(36,583);
   EtaoPcP__2->SetBinContent(37,601);
   EtaoPcP__2->SetBinContent(38,659);
   EtaoPcP__2->SetBinContent(39,581);
   EtaoPcP__2->SetBinContent(40,642);
   EtaoPcP__2->SetBinContent(41,713);
   EtaoPcP__2->SetBinContent(42,671);
   EtaoPcP__2->SetBinContent(43,657);
   EtaoPcP__2->SetBinContent(44,681);
   EtaoPcP__2->SetBinContent(45,699);
   EtaoPcP__2->SetBinContent(46,668);
   EtaoPcP__2->SetBinContent(47,717);
   EtaoPcP__2->SetBinContent(48,651);
   EtaoPcP__2->SetBinContent(49,716);
   EtaoPcP__2->SetBinContent(50,748);
   EtaoPcP__2->SetBinContent(51,721);
   EtaoPcP__2->SetBinContent(52,756);
   EtaoPcP__2->SetBinContent(53,692);
   EtaoPcP__2->SetBinContent(54,692);
   EtaoPcP__2->SetBinContent(55,739);
   EtaoPcP__2->SetBinContent(56,662);
   EtaoPcP__2->SetBinContent(57,680);
   EtaoPcP__2->SetBinContent(58,704);
   EtaoPcP__2->SetBinContent(59,687);
   EtaoPcP__2->SetBinContent(60,668);
   EtaoPcP__2->SetBinContent(61,636);
   EtaoPcP__2->SetBinContent(62,633);
   EtaoPcP__2->SetBinContent(63,606);
   EtaoPcP__2->SetBinContent(64,641);
   EtaoPcP__2->SetBinContent(65,564);
   EtaoPcP__2->SetBinContent(66,564);
   EtaoPcP__2->SetBinContent(67,551);
   EtaoPcP__2->SetBinContent(68,567);
   EtaoPcP__2->SetBinContent(69,510);
   EtaoPcP__2->SetBinContent(70,520);
   EtaoPcP__2->SetBinContent(71,526);
   EtaoPcP__2->SetBinContent(72,529);
   EtaoPcP__2->SetBinContent(73,428);
   EtaoPcP__2->SetBinContent(74,432);
   EtaoPcP__2->SetBinContent(75,381);
   EtaoPcP__2->SetBinContent(76,383);
   EtaoPcP__2->SetBinContent(77,396);
   EtaoPcP__2->SetBinContent(78,329);
   EtaoPcP__2->SetBinContent(79,306);
   EtaoPcP__2->SetBinContent(80,268);
   EtaoPcP__2->SetBinContent(81,286);
   EtaoPcP__2->SetBinContent(82,233);
   EtaoPcP__2->SetBinContent(83,244);
   EtaoPcP__2->SetBinContent(84,231);
   EtaoPcP__2->SetBinContent(85,209);
   EtaoPcP__2->SetBinContent(86,191);
   EtaoPcP__2->SetBinContent(87,196);
   EtaoPcP__2->SetBinContent(88,164);
   EtaoPcP__2->SetBinContent(89,136);
   EtaoPcP__2->SetBinContent(90,121);
   EtaoPcP__2->SetBinContent(91,129);
   EtaoPcP__2->SetBinContent(92,59);
   EtaoPcP__2->SetBinContent(93,2);
   EtaoPcP__2->SetEntries(37411);
   EtaoPcP__2->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   EtaoPcP__2->SetLineColor(ci);
   EtaoPcP__2->GetXaxis()->SetRange(1,100);
   EtaoPcP__2->GetXaxis()->SetLabelFont(42);
   EtaoPcP__2->GetXaxis()->SetTitleOffset(1);
   EtaoPcP__2->GetXaxis()->SetTitleFont(42);
   EtaoPcP__2->GetYaxis()->SetLabelFont(42);
   EtaoPcP__2->GetYaxis()->SetTitleFont(42);
   EtaoPcP__2->GetZaxis()->SetLabelFont(42);
   EtaoPcP__2->GetZaxis()->SetTitleOffset(1);
   EtaoPcP__2->GetZaxis()->SetTitleFont(42);
   EtaoPcP__2->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return EtaoPcP__2;
}

TH1F* Offline_Matched_Taus_Phi(){
  //=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Sun May 22 21:35:58 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *PhioPcP__3 = new TH1F("PhioPcP__3","Offline_Matched_Taus.Phi()",100,-3.7,3.7);
   PhioPcP__3->SetBinContent(8,206);
   PhioPcP__3->SetBinContent(9,444);
   PhioPcP__3->SetBinContent(10,482);
   PhioPcP__3->SetBinContent(11,423);
   PhioPcP__3->SetBinContent(12,406);
   PhioPcP__3->SetBinContent(13,449);
   PhioPcP__3->SetBinContent(14,450);
   PhioPcP__3->SetBinContent(15,441);
   PhioPcP__3->SetBinContent(16,448);
   PhioPcP__3->SetBinContent(17,483);
   PhioPcP__3->SetBinContent(18,472);
   PhioPcP__3->SetBinContent(19,426);
   PhioPcP__3->SetBinContent(20,386);
   PhioPcP__3->SetBinContent(21,441);
   PhioPcP__3->SetBinContent(22,470);
   PhioPcP__3->SetBinContent(23,490);
   PhioPcP__3->SetBinContent(24,421);
   PhioPcP__3->SetBinContent(25,467);
   PhioPcP__3->SetBinContent(26,481);
   PhioPcP__3->SetBinContent(27,427);
   PhioPcP__3->SetBinContent(28,421);
   PhioPcP__3->SetBinContent(29,410);
   PhioPcP__3->SetBinContent(30,459);
   PhioPcP__3->SetBinContent(31,410);
   PhioPcP__3->SetBinContent(32,461);
   PhioPcP__3->SetBinContent(33,435);
   PhioPcP__3->SetBinContent(34,431);
   PhioPcP__3->SetBinContent(35,437);
   PhioPcP__3->SetBinContent(36,454);
   PhioPcP__3->SetBinContent(37,433);
   PhioPcP__3->SetBinContent(38,474);
   PhioPcP__3->SetBinContent(39,452);
   PhioPcP__3->SetBinContent(40,403);
   PhioPcP__3->SetBinContent(41,460);
   PhioPcP__3->SetBinContent(42,469);
   PhioPcP__3->SetBinContent(43,415);
   PhioPcP__3->SetBinContent(44,419);
   PhioPcP__3->SetBinContent(45,437);
   PhioPcP__3->SetBinContent(46,429);
   PhioPcP__3->SetBinContent(47,470);
   PhioPcP__3->SetBinContent(48,382);
   PhioPcP__3->SetBinContent(49,416);
   PhioPcP__3->SetBinContent(50,443);
   PhioPcP__3->SetBinContent(51,433);
   PhioPcP__3->SetBinContent(52,423);
   PhioPcP__3->SetBinContent(53,460);
   PhioPcP__3->SetBinContent(54,428);
   PhioPcP__3->SetBinContent(55,455);
   PhioPcP__3->SetBinContent(56,430);
   PhioPcP__3->SetBinContent(57,405);
   PhioPcP__3->SetBinContent(58,486);
   PhioPcP__3->SetBinContent(59,443);
   PhioPcP__3->SetBinContent(60,433);
   PhioPcP__3->SetBinContent(61,464);
   PhioPcP__3->SetBinContent(62,419);
   PhioPcP__3->SetBinContent(63,443);
   PhioPcP__3->SetBinContent(64,426);
   PhioPcP__3->SetBinContent(65,454);
   PhioPcP__3->SetBinContent(66,427);
   PhioPcP__3->SetBinContent(67,467);
   PhioPcP__3->SetBinContent(68,420);
   PhioPcP__3->SetBinContent(69,445);
   PhioPcP__3->SetBinContent(70,431);
   PhioPcP__3->SetBinContent(71,458);
   PhioPcP__3->SetBinContent(72,445);
   PhioPcP__3->SetBinContent(73,437);
   PhioPcP__3->SetBinContent(74,445);
   PhioPcP__3->SetBinContent(75,463);
   PhioPcP__3->SetBinContent(76,452);
   PhioPcP__3->SetBinContent(77,425);
   PhioPcP__3->SetBinContent(78,447);
   PhioPcP__3->SetBinContent(79,390);
   PhioPcP__3->SetBinContent(80,444);
   PhioPcP__3->SetBinContent(81,450);
   PhioPcP__3->SetBinContent(82,427);
   PhioPcP__3->SetBinContent(83,460);
   PhioPcP__3->SetBinContent(84,439);
   PhioPcP__3->SetBinContent(85,435);
   PhioPcP__3->SetBinContent(86,419);
   PhioPcP__3->SetBinContent(87,427);
   PhioPcP__3->SetBinContent(88,414);
   PhioPcP__3->SetBinContent(89,432);
   PhioPcP__3->SetBinContent(90,445);
   PhioPcP__3->SetBinContent(91,439);
   PhioPcP__3->SetBinContent(92,500);
   PhioPcP__3->SetBinContent(93,193);
   PhioPcP__3->SetEntries(37411);
   PhioPcP__3->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   PhioPcP__3->SetLineColor(ci);
   PhioPcP__3->GetXaxis()->SetRange(1,100);
   PhioPcP__3->GetXaxis()->SetLabelFont(42);
   PhioPcP__3->GetXaxis()->SetTitleOffset(1);
   PhioPcP__3->GetXaxis()->SetTitleFont(42);
   PhioPcP__3->GetYaxis()->SetLabelFont(42);
   PhioPcP__3->GetYaxis()->SetTitleFont(42);
   PhioPcP__3->GetZaxis()->SetLabelFont(42);
   PhioPcP__3->GetZaxis()->SetTitleOffset(1);
   PhioPcP__3->GetZaxis()->SetTitleFont(42);
   PhioPcP__3->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return PhioPcP__3;
}


TH1F* Offline_Matched_Taus_Prong(){
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Sun May 22 21:47:14 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *Off_Matched_TauProng__4 = new TH1F("Off_Matched_TauProng__4","Off_Matched_TauProng.Off_Matched_TauProng",24,0,24);
   Off_Matched_TauProng__4->SetBinContent(1,1865);
   Off_Matched_TauProng__4->SetBinContent(2,25990);
   Off_Matched_TauProng__4->SetBinContent(3,2104);
   Off_Matched_TauProng__4->SetBinContent(4,6921);
   Off_Matched_TauProng__4->SetBinContent(5,208);
   Off_Matched_TauProng__4->SetBinContent(6,129);
   Off_Matched_TauProng__4->SetBinContent(7,63);
   Off_Matched_TauProng__4->SetBinContent(8,39);
   Off_Matched_TauProng__4->SetBinContent(9,38);
   Off_Matched_TauProng__4->SetBinContent(10,19);
   Off_Matched_TauProng__4->SetBinContent(11,13);
   Off_Matched_TauProng__4->SetBinContent(12,11);
   Off_Matched_TauProng__4->SetBinContent(13,5);
   Off_Matched_TauProng__4->SetBinContent(14,2);
   Off_Matched_TauProng__4->SetBinContent(15,2);
   Off_Matched_TauProng__4->SetBinContent(19,1);
   Off_Matched_TauProng__4->SetBinContent(23,1);
   Off_Matched_TauProng__4->SetEntries(37411);
   Off_Matched_TauProng__4->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Off_Matched_TauProng__4->SetLineColor(ci);
   Off_Matched_TauProng__4->GetXaxis()->SetRange(1,100);
   Off_Matched_TauProng__4->GetXaxis()->SetLabelFont(42);
   Off_Matched_TauProng__4->GetXaxis()->SetTitleOffset(1);
   Off_Matched_TauProng__4->GetXaxis()->SetTitleFont(42);
   Off_Matched_TauProng__4->GetYaxis()->SetLabelFont(42);
   Off_Matched_TauProng__4->GetYaxis()->SetTitleFont(42);
   Off_Matched_TauProng__4->GetZaxis()->SetLabelFont(42);
   Off_Matched_TauProng__4->GetZaxis()->SetTitleOffset(1);
   Off_Matched_TauProng__4->GetZaxis()->SetTitleFont(42);
   Off_Matched_TauProng__4->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return Off_Matched_TauProng__4;
}


TH1F* Offline_Matched_Taus_RNN(){
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Sun May 22 21:50:20 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *Off_Matched_TauRNN__6 = new TH1F("Off_Matched_TauRNN__6","Off_Matched_TauRNN.Off_Matched_TauRNN",100,0,1.08);
   Off_Matched_TauRNN__6->SetBinContent(1,3171);
   Off_Matched_TauRNN__6->SetBinContent(2,662);
   Off_Matched_TauRNN__6->SetBinContent(3,559);
   Off_Matched_TauRNN__6->SetBinContent(4,544);
   Off_Matched_TauRNN__6->SetBinContent(5,509);
   Off_Matched_TauRNN__6->SetBinContent(6,451);
   Off_Matched_TauRNN__6->SetBinContent(7,466);
   Off_Matched_TauRNN__6->SetBinContent(8,464);
   Off_Matched_TauRNN__6->SetBinContent(9,398);
   Off_Matched_TauRNN__6->SetBinContent(10,398);
   Off_Matched_TauRNN__6->SetBinContent(11,408);
   Off_Matched_TauRNN__6->SetBinContent(12,363);
   Off_Matched_TauRNN__6->SetBinContent(13,408);
   Off_Matched_TauRNN__6->SetBinContent(14,379);
   Off_Matched_TauRNN__6->SetBinContent(15,434);
   Off_Matched_TauRNN__6->SetBinContent(16,372);
   Off_Matched_TauRNN__6->SetBinContent(17,372);
   Off_Matched_TauRNN__6->SetBinContent(18,379);
   Off_Matched_TauRNN__6->SetBinContent(19,358);
   Off_Matched_TauRNN__6->SetBinContent(20,349);
   Off_Matched_TauRNN__6->SetBinContent(21,348);
   Off_Matched_TauRNN__6->SetBinContent(22,344);
   Off_Matched_TauRNN__6->SetBinContent(23,354);
   Off_Matched_TauRNN__6->SetBinContent(24,373);
   Off_Matched_TauRNN__6->SetBinContent(25,333);
   Off_Matched_TauRNN__6->SetBinContent(26,336);
   Off_Matched_TauRNN__6->SetBinContent(27,369);
   Off_Matched_TauRNN__6->SetBinContent(28,314);
   Off_Matched_TauRNN__6->SetBinContent(29,313);
   Off_Matched_TauRNN__6->SetBinContent(30,353);
   Off_Matched_TauRNN__6->SetBinContent(31,307);
   Off_Matched_TauRNN__6->SetBinContent(32,333);
   Off_Matched_TauRNN__6->SetBinContent(33,361);
   Off_Matched_TauRNN__6->SetBinContent(34,356);
   Off_Matched_TauRNN__6->SetBinContent(35,342);
   Off_Matched_TauRNN__6->SetBinContent(36,365);
   Off_Matched_TauRNN__6->SetBinContent(37,341);
   Off_Matched_TauRNN__6->SetBinContent(38,326);
   Off_Matched_TauRNN__6->SetBinContent(39,330);
   Off_Matched_TauRNN__6->SetBinContent(40,321);
   Off_Matched_TauRNN__6->SetBinContent(41,376);
   Off_Matched_TauRNN__6->SetBinContent(42,387);
   Off_Matched_TauRNN__6->SetBinContent(43,306);
   Off_Matched_TauRNN__6->SetBinContent(44,378);
   Off_Matched_TauRNN__6->SetBinContent(45,311);
   Off_Matched_TauRNN__6->SetBinContent(46,361);
   Off_Matched_TauRNN__6->SetBinContent(47,365);
   Off_Matched_TauRNN__6->SetBinContent(48,337);
   Off_Matched_TauRNN__6->SetBinContent(49,343);
   Off_Matched_TauRNN__6->SetBinContent(50,310);
   Off_Matched_TauRNN__6->SetBinContent(51,345);
   Off_Matched_TauRNN__6->SetBinContent(52,328);
   Off_Matched_TauRNN__6->SetBinContent(53,349);
   Off_Matched_TauRNN__6->SetBinContent(54,363);
   Off_Matched_TauRNN__6->SetBinContent(55,333);
   Off_Matched_TauRNN__6->SetBinContent(56,373);
   Off_Matched_TauRNN__6->SetBinContent(57,336);
   Off_Matched_TauRNN__6->SetBinContent(58,364);
   Off_Matched_TauRNN__6->SetBinContent(59,366);
   Off_Matched_TauRNN__6->SetBinContent(60,351);
   Off_Matched_TauRNN__6->SetBinContent(61,343);
   Off_Matched_TauRNN__6->SetBinContent(62,377);
   Off_Matched_TauRNN__6->SetBinContent(63,362);
   Off_Matched_TauRNN__6->SetBinContent(64,356);
   Off_Matched_TauRNN__6->SetBinContent(65,364);
   Off_Matched_TauRNN__6->SetBinContent(66,387);
   Off_Matched_TauRNN__6->SetBinContent(67,378);
   Off_Matched_TauRNN__6->SetBinContent(68,351);
   Off_Matched_TauRNN__6->SetBinContent(69,374);
   Off_Matched_TauRNN__6->SetBinContent(70,362);
   Off_Matched_TauRNN__6->SetBinContent(71,376);
   Off_Matched_TauRNN__6->SetBinContent(72,403);
   Off_Matched_TauRNN__6->SetBinContent(73,337);
   Off_Matched_TauRNN__6->SetBinContent(74,340);
   Off_Matched_TauRNN__6->SetBinContent(75,391);
   Off_Matched_TauRNN__6->SetBinContent(76,365);
   Off_Matched_TauRNN__6->SetBinContent(77,357);
   Off_Matched_TauRNN__6->SetBinContent(78,384);
   Off_Matched_TauRNN__6->SetBinContent(79,354);
   Off_Matched_TauRNN__6->SetBinContent(80,318);
   Off_Matched_TauRNN__6->SetBinContent(81,366);
   Off_Matched_TauRNN__6->SetBinContent(82,368);
   Off_Matched_TauRNN__6->SetBinContent(83,381);
   Off_Matched_TauRNN__6->SetBinContent(84,363);
   Off_Matched_TauRNN__6->SetBinContent(85,361);
   Off_Matched_TauRNN__6->SetBinContent(86,407);
   Off_Matched_TauRNN__6->SetBinContent(87,350);
   Off_Matched_TauRNN__6->SetBinContent(88,403);
   Off_Matched_TauRNN__6->SetBinContent(89,392);
   Off_Matched_TauRNN__6->SetBinContent(90,391);
   Off_Matched_TauRNN__6->SetBinContent(91,399);
   Off_Matched_TauRNN__6->SetBinContent(92,609);
   Off_Matched_TauRNN__6->SetBinContent(93,97);
   Off_Matched_TauRNN__6->SetEntries(37411);
   Off_Matched_TauRNN__6->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Off_Matched_TauRNN__6->SetLineColor(ci);
   Off_Matched_TauRNN__6->GetXaxis()->SetRange(1,100);
   Off_Matched_TauRNN__6->GetXaxis()->SetLabelFont(42);
   Off_Matched_TauRNN__6->GetXaxis()->SetTitleOffset(1);
   Off_Matched_TauRNN__6->GetXaxis()->SetTitleFont(42);
   Off_Matched_TauRNN__6->GetYaxis()->SetLabelFont(42);
   Off_Matched_TauRNN__6->GetYaxis()->SetTitleFont(42);
   Off_Matched_TauRNN__6->GetZaxis()->SetLabelFont(42);
   Off_Matched_TauRNN__6->GetZaxis()->SetTitleOffset(1);
   Off_Matched_TauRNN__6->GetZaxis()->SetTitleFont(42);
   Off_Matched_TauRNN__6->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return Off_Matched_TauRNN__6;
}

//================Offline_Matched_Taus=================


//===============TrigMatched_Taus_HLTetafl====================

TH1F* TrigMatched_Taus_HLTetafl_Pt()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 02:42:02 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",1,1,4,4);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *PtoPcP__1 = new TH1F("PtoPcP__1","TrigMatched_Taus_HLTetafl.Pt()",100,0,1040);
   PtoPcP__1->SetBinContent(3,962);
   PtoPcP__1->SetBinContent(4,1689);
   PtoPcP__1->SetBinContent(5,1487);
   PtoPcP__1->SetBinContent(6,1261);
   PtoPcP__1->SetBinContent(7,994);
   PtoPcP__1->SetBinContent(8,838);
   PtoPcP__1->SetBinContent(9,673);
   PtoPcP__1->SetBinContent(10,572);
   PtoPcP__1->SetBinContent(11,389);
   PtoPcP__1->SetBinContent(12,352);
   PtoPcP__1->SetBinContent(13,287);
   PtoPcP__1->SetBinContent(14,222);
   PtoPcP__1->SetBinContent(15,176);
   PtoPcP__1->SetBinContent(16,152);
   PtoPcP__1->SetBinContent(17,121);
   PtoPcP__1->SetBinContent(18,78);
   PtoPcP__1->SetBinContent(19,69);
   PtoPcP__1->SetBinContent(20,56);
   PtoPcP__1->SetBinContent(21,46);
   PtoPcP__1->SetBinContent(22,42);
   PtoPcP__1->SetBinContent(23,34);
   PtoPcP__1->SetBinContent(24,28);
   PtoPcP__1->SetBinContent(25,16);
   PtoPcP__1->SetBinContent(26,18);
   PtoPcP__1->SetBinContent(27,13);
   PtoPcP__1->SetBinContent(28,11);
   PtoPcP__1->SetBinContent(29,8);
   PtoPcP__1->SetBinContent(30,11);
   PtoPcP__1->SetBinContent(31,5);
   PtoPcP__1->SetBinContent(32,11);
   PtoPcP__1->SetBinContent(33,7);
   PtoPcP__1->SetBinContent(34,5);
   PtoPcP__1->SetBinContent(35,8);
   PtoPcP__1->SetBinContent(36,4);
   PtoPcP__1->SetBinContent(37,3);
   PtoPcP__1->SetBinContent(38,7);
   PtoPcP__1->SetBinContent(39,1);
   PtoPcP__1->SetBinContent(40,1);
   PtoPcP__1->SetBinContent(41,2);
   PtoPcP__1->SetBinContent(43,8);
   PtoPcP__1->SetBinContent(44,9);
   PtoPcP__1->SetBinContent(45,8);
   PtoPcP__1->SetBinContent(46,4);
   PtoPcP__1->SetBinContent(47,3);
   PtoPcP__1->SetBinContent(48,7);
   PtoPcP__1->SetBinContent(49,2);
   PtoPcP__1->SetBinContent(50,1);
   PtoPcP__1->SetBinContent(51,4);
   PtoPcP__1->SetBinContent(52,2);
   PtoPcP__1->SetBinContent(53,1);
   PtoPcP__1->SetBinContent(54,1);
   PtoPcP__1->SetBinContent(56,5);
   PtoPcP__1->SetBinContent(57,1);
   PtoPcP__1->SetBinContent(58,2);
   PtoPcP__1->SetBinContent(61,2);
   PtoPcP__1->SetBinContent(63,2);
   PtoPcP__1->SetBinContent(64,3);
   PtoPcP__1->SetBinContent(65,2);
   PtoPcP__1->SetBinContent(70,1);
   PtoPcP__1->SetBinContent(73,1);
   PtoPcP__1->SetBinContent(74,1);
   PtoPcP__1->SetBinContent(75,2);
   PtoPcP__1->SetBinContent(77,1);
   PtoPcP__1->SetBinContent(81,1);
   PtoPcP__1->SetBinContent(88,1);
   PtoPcP__1->SetBinContent(90,1);
   PtoPcP__1->SetBinContent(91,1);
   PtoPcP__1->SetBinContent(93,1);
   PtoPcP__1->SetEntries(10737);
   PtoPcP__1->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   PtoPcP__1->SetLineColor(ci);
   PtoPcP__1->GetXaxis()->SetRange(1,100);
   PtoPcP__1->GetXaxis()->SetLabelFont(42);
   PtoPcP__1->GetXaxis()->SetTitleOffset(1);
   PtoPcP__1->GetXaxis()->SetTitleFont(42);
   PtoPcP__1->GetYaxis()->SetLabelFont(42);
   PtoPcP__1->GetYaxis()->SetTitleFont(42);
   PtoPcP__1->GetZaxis()->SetLabelFont(42);
   PtoPcP__1->GetZaxis()->SetTitleOffset(1);
   PtoPcP__1->GetZaxis()->SetTitleFont(42);
   PtoPcP__1->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return PtoPcP__1;
}

TH1F* TrigMatched_Taus_HLTetafl_Eta()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 02:43:50 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *EtaoPcP__2 = new TH1F("EtaoPcP__2","TrigMatched_Taus_HLTetafl.Eta()",100,-3,3);
   EtaoPcP__2->SetBinContent(8,8);
   EtaoPcP__2->SetBinContent(9,27);
   EtaoPcP__2->SetBinContent(10,29);
   EtaoPcP__2->SetBinContent(11,29);
   EtaoPcP__2->SetBinContent(12,43);
   EtaoPcP__2->SetBinContent(13,40);
   EtaoPcP__2->SetBinContent(14,41);
   EtaoPcP__2->SetBinContent(15,42);
   EtaoPcP__2->SetBinContent(16,59);
   EtaoPcP__2->SetBinContent(17,56);
   EtaoPcP__2->SetBinContent(18,68);
   EtaoPcP__2->SetBinContent(19,51);
   EtaoPcP__2->SetBinContent(20,77);
   EtaoPcP__2->SetBinContent(21,65);
   EtaoPcP__2->SetBinContent(22,73);
   EtaoPcP__2->SetBinContent(23,76);
   EtaoPcP__2->SetBinContent(24,69);
   EtaoPcP__2->SetBinContent(25,64);
   EtaoPcP__2->SetBinContent(26,84);
   EtaoPcP__2->SetBinContent(27,108);
   EtaoPcP__2->SetBinContent(28,113);
   EtaoPcP__2->SetBinContent(29,141);
   EtaoPcP__2->SetBinContent(30,108);
   EtaoPcP__2->SetBinContent(31,135);
   EtaoPcP__2->SetBinContent(32,147);
   EtaoPcP__2->SetBinContent(33,141);
   EtaoPcP__2->SetBinContent(34,151);
   EtaoPcP__2->SetBinContent(35,153);
   EtaoPcP__2->SetBinContent(36,163);
   EtaoPcP__2->SetBinContent(37,187);
   EtaoPcP__2->SetBinContent(38,200);
   EtaoPcP__2->SetBinContent(39,188);
   EtaoPcP__2->SetBinContent(40,187);
   EtaoPcP__2->SetBinContent(41,196);
   EtaoPcP__2->SetBinContent(42,220);
   EtaoPcP__2->SetBinContent(43,244);
   EtaoPcP__2->SetBinContent(44,198);
   EtaoPcP__2->SetBinContent(45,201);
   EtaoPcP__2->SetBinContent(46,246);
   EtaoPcP__2->SetBinContent(47,206);
   EtaoPcP__2->SetBinContent(48,225);
   EtaoPcP__2->SetBinContent(49,227);
   EtaoPcP__2->SetBinContent(50,260);
   EtaoPcP__2->SetBinContent(51,227);
   EtaoPcP__2->SetBinContent(52,239);
   EtaoPcP__2->SetBinContent(53,225);
   EtaoPcP__2->SetBinContent(54,192);
   EtaoPcP__2->SetBinContent(55,258);
   EtaoPcP__2->SetBinContent(56,192);
   EtaoPcP__2->SetBinContent(57,218);
   EtaoPcP__2->SetBinContent(58,222);
   EtaoPcP__2->SetBinContent(59,210);
   EtaoPcP__2->SetBinContent(60,223);
   EtaoPcP__2->SetBinContent(61,192);
   EtaoPcP__2->SetBinContent(62,193);
   EtaoPcP__2->SetBinContent(63,190);
   EtaoPcP__2->SetBinContent(64,187);
   EtaoPcP__2->SetBinContent(65,164);
   EtaoPcP__2->SetBinContent(66,151);
   EtaoPcP__2->SetBinContent(67,139);
   EtaoPcP__2->SetBinContent(68,167);
   EtaoPcP__2->SetBinContent(69,147);
   EtaoPcP__2->SetBinContent(70,130);
   EtaoPcP__2->SetBinContent(71,143);
   EtaoPcP__2->SetBinContent(72,139);
   EtaoPcP__2->SetBinContent(73,106);
   EtaoPcP__2->SetBinContent(74,122);
   EtaoPcP__2->SetBinContent(75,91);
   EtaoPcP__2->SetBinContent(76,64);
   EtaoPcP__2->SetBinContent(77,72);
   EtaoPcP__2->SetBinContent(78,94);
   EtaoPcP__2->SetBinContent(79,63);
   EtaoPcP__2->SetBinContent(80,78);
   EtaoPcP__2->SetBinContent(81,71);
   EtaoPcP__2->SetBinContent(82,65);
   EtaoPcP__2->SetBinContent(83,71);
   EtaoPcP__2->SetBinContent(84,65);
   EtaoPcP__2->SetBinContent(85,56);
   EtaoPcP__2->SetBinContent(86,46);
   EtaoPcP__2->SetBinContent(87,35);
   EtaoPcP__2->SetBinContent(88,30);
   EtaoPcP__2->SetBinContent(89,37);
   EtaoPcP__2->SetBinContent(90,25);
   EtaoPcP__2->SetBinContent(91,26);
   EtaoPcP__2->SetBinContent(92,22);
   EtaoPcP__2->SetBinContent(93,4);
   EtaoPcP__2->SetEntries(10737);
   EtaoPcP__2->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   EtaoPcP__2->SetLineColor(ci);
   EtaoPcP__2->GetXaxis()->SetRange(1,100);
   EtaoPcP__2->GetXaxis()->SetLabelFont(42);
   EtaoPcP__2->GetXaxis()->SetTitleOffset(1);
   EtaoPcP__2->GetXaxis()->SetTitleFont(42);
   EtaoPcP__2->GetYaxis()->SetLabelFont(42);
   EtaoPcP__2->GetYaxis()->SetTitleFont(42);
   EtaoPcP__2->GetZaxis()->SetLabelFont(42);
   EtaoPcP__2->GetZaxis()->SetTitleOffset(1);
   EtaoPcP__2->GetZaxis()->SetTitleFont(42);
   EtaoPcP__2->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return EtaoPcP__2;
}

#ifdef __CLING__
#pragma cling optimize(0)
#endif
TH1F* TrigMatched_Taus_HLTetafl_Phi()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 02:45:26 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *PhioPcP__3 = new TH1F("PhioPcP__3","TrigMatched_Taus_HLTetafl.Phi()",100,-3.7,3.7);
   PhioPcP__3->SetBinContent(8,45);
   PhioPcP__3->SetBinContent(9,144);
   PhioPcP__3->SetBinContent(10,167);
   PhioPcP__3->SetBinContent(11,121);
   PhioPcP__3->SetBinContent(12,106);
   PhioPcP__3->SetBinContent(13,125);
   PhioPcP__3->SetBinContent(14,120);
   PhioPcP__3->SetBinContent(15,144);
   PhioPcP__3->SetBinContent(16,119);
   PhioPcP__3->SetBinContent(17,137);
   PhioPcP__3->SetBinContent(18,140);
   PhioPcP__3->SetBinContent(19,125);
   PhioPcP__3->SetBinContent(20,127);
   PhioPcP__3->SetBinContent(21,133);
   PhioPcP__3->SetBinContent(22,137);
   PhioPcP__3->SetBinContent(23,133);
   PhioPcP__3->SetBinContent(24,127);
   PhioPcP__3->SetBinContent(25,136);
   PhioPcP__3->SetBinContent(26,148);
   PhioPcP__3->SetBinContent(27,125);
   PhioPcP__3->SetBinContent(28,121);
   PhioPcP__3->SetBinContent(29,125);
   PhioPcP__3->SetBinContent(30,143);
   PhioPcP__3->SetBinContent(31,130);
   PhioPcP__3->SetBinContent(32,116);
   PhioPcP__3->SetBinContent(33,125);
   PhioPcP__3->SetBinContent(34,122);
   PhioPcP__3->SetBinContent(35,136);
   PhioPcP__3->SetBinContent(36,125);
   PhioPcP__3->SetBinContent(37,123);
   PhioPcP__3->SetBinContent(38,150);
   PhioPcP__3->SetBinContent(39,118);
   PhioPcP__3->SetBinContent(40,99);
   PhioPcP__3->SetBinContent(41,129);
   PhioPcP__3->SetBinContent(42,125);
   PhioPcP__3->SetBinContent(43,125);
   PhioPcP__3->SetBinContent(44,111);
   PhioPcP__3->SetBinContent(45,109);
   PhioPcP__3->SetBinContent(46,122);
   PhioPcP__3->SetBinContent(47,164);
   PhioPcP__3->SetBinContent(48,107);
   PhioPcP__3->SetBinContent(49,108);
   PhioPcP__3->SetBinContent(50,127);
   PhioPcP__3->SetBinContent(51,118);
   PhioPcP__3->SetBinContent(52,123);
   PhioPcP__3->SetBinContent(53,132);
   PhioPcP__3->SetBinContent(54,126);
   PhioPcP__3->SetBinContent(55,145);
   PhioPcP__3->SetBinContent(56,109);
   PhioPcP__3->SetBinContent(57,99);
   PhioPcP__3->SetBinContent(58,142);
   PhioPcP__3->SetBinContent(59,144);
   PhioPcP__3->SetBinContent(60,120);
   PhioPcP__3->SetBinContent(61,130);
   PhioPcP__3->SetBinContent(62,129);
   PhioPcP__3->SetBinContent(63,115);
   PhioPcP__3->SetBinContent(64,117);
   PhioPcP__3->SetBinContent(65,114);
   PhioPcP__3->SetBinContent(66,140);
   PhioPcP__3->SetBinContent(67,150);
   PhioPcP__3->SetBinContent(68,133);
   PhioPcP__3->SetBinContent(69,107);
   PhioPcP__3->SetBinContent(70,121);
   PhioPcP__3->SetBinContent(71,136);
   PhioPcP__3->SetBinContent(72,138);
   PhioPcP__3->SetBinContent(73,125);
   PhioPcP__3->SetBinContent(74,122);
   PhioPcP__3->SetBinContent(75,129);
   PhioPcP__3->SetBinContent(76,124);
   PhioPcP__3->SetBinContent(77,100);
   PhioPcP__3->SetBinContent(78,126);
   PhioPcP__3->SetBinContent(79,123);
   PhioPcP__3->SetBinContent(80,128);
   PhioPcP__3->SetBinContent(81,127);
   PhioPcP__3->SetBinContent(82,123);
   PhioPcP__3->SetBinContent(83,139);
   PhioPcP__3->SetBinContent(84,134);
   PhioPcP__3->SetBinContent(85,121);
   PhioPcP__3->SetBinContent(86,115);
   PhioPcP__3->SetBinContent(87,116);
   PhioPcP__3->SetBinContent(88,127);
   PhioPcP__3->SetBinContent(89,122);
   PhioPcP__3->SetBinContent(90,101);
   PhioPcP__3->SetBinContent(91,137);
   PhioPcP__3->SetBinContent(92,136);
   PhioPcP__3->SetBinContent(93,55);
   PhioPcP__3->SetEntries(10737);
   PhioPcP__3->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   PhioPcP__3->SetLineColor(ci);
   PhioPcP__3->GetXaxis()->SetRange(1,100);
   PhioPcP__3->GetXaxis()->SetLabelFont(42);
   PhioPcP__3->GetXaxis()->SetTitleOffset(1);
   PhioPcP__3->GetXaxis()->SetTitleFont(42);
   PhioPcP__3->GetYaxis()->SetLabelFont(42);
   PhioPcP__3->GetYaxis()->SetTitleFont(42);
   PhioPcP__3->GetZaxis()->SetLabelFont(42);
   PhioPcP__3->GetZaxis()->SetTitleOffset(1);
   PhioPcP__3->GetZaxis()->SetTitleFont(42);
   PhioPcP__3->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return PhioPcP__3;
}

#ifdef __CLING__
#pragma cling optimize(0)
#endif
TH1F* TrigMatched_prong_HLTetafl()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 02:47:45 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *TrigMatched_prong_HLTetafl__4 = new TH1F("TrigMatched_prong_HLTetafl__4","TrigMatched_prong_HLTetafl.TrigMatched_prong_HLTetafl",29,0,29);
   TrigMatched_prong_HLTetafl__4->SetBinContent(1,144);
   TrigMatched_prong_HLTetafl__4->SetBinContent(2,7065);
   TrigMatched_prong_HLTetafl__4->SetBinContent(3,1403);
   TrigMatched_prong_HLTetafl__4->SetBinContent(4,2068);
   TrigMatched_prong_HLTetafl__4->SetBinContent(5,8);
   TrigMatched_prong_HLTetafl__4->SetBinContent(6,3);
   TrigMatched_prong_HLTetafl__4->SetBinContent(7,2);
   TrigMatched_prong_HLTetafl__4->SetBinContent(8,6);
   TrigMatched_prong_HLTetafl__4->SetBinContent(9,8);
   TrigMatched_prong_HLTetafl__4->SetBinContent(10,1);
   TrigMatched_prong_HLTetafl__4->SetBinContent(11,3);
   TrigMatched_prong_HLTetafl__4->SetBinContent(12,1);
   TrigMatched_prong_HLTetafl__4->SetBinContent(13,2);
   TrigMatched_prong_HLTetafl__4->SetBinContent(14,3);
   TrigMatched_prong_HLTetafl__4->SetBinContent(15,3);
   TrigMatched_prong_HLTetafl__4->SetBinContent(16,4);
   TrigMatched_prong_HLTetafl__4->SetBinContent(17,1);
   TrigMatched_prong_HLTetafl__4->SetBinContent(18,5);
   TrigMatched_prong_HLTetafl__4->SetBinContent(19,1);
   TrigMatched_prong_HLTetafl__4->SetBinContent(20,1);
   TrigMatched_prong_HLTetafl__4->SetBinContent(22,2);
   TrigMatched_prong_HLTetafl__4->SetBinContent(23,2);
   TrigMatched_prong_HLTetafl__4->SetBinContent(28,1);
   TrigMatched_prong_HLTetafl__4->SetEntries(10737);
   TrigMatched_prong_HLTetafl__4->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   TrigMatched_prong_HLTetafl__4->SetLineColor(ci);
   TrigMatched_prong_HLTetafl__4->GetXaxis()->SetRange(1,100);
   TrigMatched_prong_HLTetafl__4->GetXaxis()->SetLabelFont(42);
   TrigMatched_prong_HLTetafl__4->GetXaxis()->SetTitleOffset(1);
   TrigMatched_prong_HLTetafl__4->GetXaxis()->SetTitleFont(42);
   TrigMatched_prong_HLTetafl__4->GetYaxis()->SetLabelFont(42);
   TrigMatched_prong_HLTetafl__4->GetYaxis()->SetTitleFont(42);
   TrigMatched_prong_HLTetafl__4->GetZaxis()->SetLabelFont(42);
   TrigMatched_prong_HLTetafl__4->GetZaxis()->SetTitleOffset(1);
   TrigMatched_prong_HLTetafl__4->GetZaxis()->SetTitleFont(42);
   TrigMatched_prong_HLTetafl__4->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return TrigMatched_prong_HLTetafl__4;
}

#ifdef __CLING__
#pragma cling optimize(0)
#endif
TH1F* TrigMatched_rnn_HLTetafl()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 02:49:25 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *TrigMatched_rnn_HLTetafl__5 = new TH1F("TrigMatched_rnn_HLTetafl__5","TrigMatched_rnn_HLTetafl.TrigMatched_rnn_HLTetafl",100,0,1.08);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(1,46);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(2,11);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(3,9);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(4,138);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(5,155);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(6,159);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(7,135);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(8,135);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(9,134);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(10,153);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(11,147);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(12,134);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(13,158);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(14,192);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(15,216);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(16,219);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(17,192);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(18,164);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(19,198);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(20,190);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(21,174);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(22,187);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(23,204);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(24,182);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(25,161);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(26,159);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(27,156);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(28,137);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(29,161);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(30,148);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(31,130);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(32,130);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(33,120);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(34,138);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(35,126);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(36,122);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(37,115);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(38,94);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(39,99);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(40,83);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(41,105);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(42,100);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(43,94);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(44,95);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(45,85);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(46,74);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(47,91);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(48,78);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(49,73);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(50,69);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(51,97);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(52,67);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(53,76);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(54,66);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(55,61);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(56,77);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(57,71);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(58,71);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(59,79);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(60,80);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(61,66);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(62,65);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(63,76);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(64,78);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(65,80);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(66,80);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(67,79);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(68,70);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(69,76);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(70,86);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(71,74);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(72,75);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(73,84);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(74,85);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(75,101);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(76,107);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(77,82);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(78,110);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(79,82);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(80,120);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(81,110);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(82,103);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(83,126);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(84,107);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(85,132);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(86,120);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(87,129);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(88,137);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(89,129);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(90,151);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(91,170);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(92,325);
   TrigMatched_rnn_HLTetafl__5->SetBinContent(93,2);
   TrigMatched_rnn_HLTetafl__5->SetEntries(10737);
   TrigMatched_rnn_HLTetafl__5->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   TrigMatched_rnn_HLTetafl__5->SetLineColor(ci);
   TrigMatched_rnn_HLTetafl__5->GetXaxis()->SetRange(1,100);
   TrigMatched_rnn_HLTetafl__5->GetXaxis()->SetLabelFont(42);
   TrigMatched_rnn_HLTetafl__5->GetXaxis()->SetTitleOffset(1);
   TrigMatched_rnn_HLTetafl__5->GetXaxis()->SetTitleFont(42);
   TrigMatched_rnn_HLTetafl__5->GetYaxis()->SetLabelFont(42);
   TrigMatched_rnn_HLTetafl__5->GetYaxis()->SetTitleFont(42);
   TrigMatched_rnn_HLTetafl__5->GetZaxis()->SetLabelFont(42);
   TrigMatched_rnn_HLTetafl__5->GetZaxis()->SetTitleOffset(1);
   TrigMatched_rnn_HLTetafl__5->GetZaxis()->SetTitleFont(42);
   TrigMatched_rnn_HLTetafl__5->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return TrigMatched_rnn_HLTetafl__5;
}

//============================================================

//============================================================

TH1F* TrigMatched_Taus_HLTptfl_Pt()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 03:19:53 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *PtoPcP__6 = new TH1F("PtoPcP__6","TrigMatched_Taus_HLTptfl.Pt()",100,0,1020);
   PtoPcP__6->SetBinContent(3,988);
   PtoPcP__6->SetBinContent(4,2016);
   PtoPcP__6->SetBinContent(5,1812);
   PtoPcP__6->SetBinContent(6,1502);
   PtoPcP__6->SetBinContent(7,1252);
   PtoPcP__6->SetBinContent(8,1010);
   PtoPcP__6->SetBinContent(9,812);
   PtoPcP__6->SetBinContent(10,670);
   PtoPcP__6->SetBinContent(11,514);
   PtoPcP__6->SetBinContent(12,426);
   PtoPcP__6->SetBinContent(13,344);
   PtoPcP__6->SetBinContent(14,259);
   PtoPcP__6->SetBinContent(15,208);
   PtoPcP__6->SetBinContent(16,174);
   PtoPcP__6->SetBinContent(17,137);
   PtoPcP__6->SetBinContent(18,94);
   PtoPcP__6->SetBinContent(19,77);
   PtoPcP__6->SetBinContent(20,71);
   PtoPcP__6->SetBinContent(21,51);
   PtoPcP__6->SetBinContent(22,52);
   PtoPcP__6->SetBinContent(23,32);
   PtoPcP__6->SetBinContent(24,32);
   PtoPcP__6->SetBinContent(25,27);
   PtoPcP__6->SetBinContent(26,15);
   PtoPcP__6->SetBinContent(27,11);
   PtoPcP__6->SetBinContent(28,9);
   PtoPcP__6->SetBinContent(29,11);
   PtoPcP__6->SetBinContent(30,14);
   PtoPcP__6->SetBinContent(31,4);
   PtoPcP__6->SetBinContent(32,10);
   PtoPcP__6->SetBinContent(33,5);
   PtoPcP__6->SetBinContent(34,5);
   PtoPcP__6->SetBinContent(35,8);
   PtoPcP__6->SetBinContent(36,9);
   PtoPcP__6->SetBinContent(37,4);
   PtoPcP__6->SetBinContent(38,2);
   PtoPcP__6->SetBinContent(39,5);
   PtoPcP__6->SetBinContent(40,1);
   PtoPcP__6->SetBinContent(41,3);
   PtoPcP__6->SetBinContent(44,5);
   PtoPcP__6->SetBinContent(45,3);
   PtoPcP__6->SetBinContent(46,5);
   PtoPcP__6->SetBinContent(47,3);
   PtoPcP__6->SetBinContent(48,3);
   PtoPcP__6->SetBinContent(49,4);
   PtoPcP__6->SetBinContent(50,1);
   PtoPcP__6->SetBinContent(51,1);
   PtoPcP__6->SetBinContent(52,2);
   PtoPcP__6->SetBinContent(53,2);
   PtoPcP__6->SetBinContent(54,1);
   PtoPcP__6->SetBinContent(57,1);
   PtoPcP__6->SetBinContent(58,1);
   PtoPcP__6->SetBinContent(62,1);
   PtoPcP__6->SetBinContent(64,1);
   PtoPcP__6->SetBinContent(65,1);
   PtoPcP__6->SetBinContent(66,1);
   PtoPcP__6->SetBinContent(71,1);
   PtoPcP__6->SetBinContent(75,1);
   PtoPcP__6->SetBinContent(77,1);
   PtoPcP__6->SetBinContent(90,1);
   PtoPcP__6->SetBinContent(92,1);
   PtoPcP__6->SetEntries(12717);
   PtoPcP__6->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   PtoPcP__6->SetLineColor(ci);
   PtoPcP__6->GetXaxis()->SetRange(1,100);
   PtoPcP__6->GetXaxis()->SetLabelFont(42);
   PtoPcP__6->GetXaxis()->SetTitleOffset(1);
   PtoPcP__6->GetXaxis()->SetTitleFont(42);
   PtoPcP__6->GetYaxis()->SetLabelFont(42);
   PtoPcP__6->GetYaxis()->SetTitleFont(42);
   PtoPcP__6->GetZaxis()->SetLabelFont(42);
   PtoPcP__6->GetZaxis()->SetTitleOffset(1);
   PtoPcP__6->GetZaxis()->SetTitleFont(42);
   PtoPcP__6->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return PtoPcP__6;
}

#ifdef __CLING__
#pragma cling optimize(0)
#endif
TH1F* TrigMatched_Taus_HLTptfl_Eta()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 03:21:22 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *EtaoPcP__7 = new TH1F("EtaoPcP__7","TrigMatched_Taus_HLTptfl.Eta()",100,-3,3);
   EtaoPcP__7->SetBinContent(8,3);
   EtaoPcP__7->SetBinContent(9,31);
   EtaoPcP__7->SetBinContent(10,29);
   EtaoPcP__7->SetBinContent(11,37);
   EtaoPcP__7->SetBinContent(12,47);
   EtaoPcP__7->SetBinContent(13,52);
   EtaoPcP__7->SetBinContent(14,50);
   EtaoPcP__7->SetBinContent(15,45);
   EtaoPcP__7->SetBinContent(16,67);
   EtaoPcP__7->SetBinContent(17,65);
   EtaoPcP__7->SetBinContent(18,78);
   EtaoPcP__7->SetBinContent(19,65);
   EtaoPcP__7->SetBinContent(20,88);
   EtaoPcP__7->SetBinContent(21,87);
   EtaoPcP__7->SetBinContent(22,80);
   EtaoPcP__7->SetBinContent(23,85);
   EtaoPcP__7->SetBinContent(24,86);
   EtaoPcP__7->SetBinContent(25,77);
   EtaoPcP__7->SetBinContent(26,91);
   EtaoPcP__7->SetBinContent(27,134);
   EtaoPcP__7->SetBinContent(28,135);
   EtaoPcP__7->SetBinContent(29,164);
   EtaoPcP__7->SetBinContent(30,125);
   EtaoPcP__7->SetBinContent(31,148);
   EtaoPcP__7->SetBinContent(32,172);
   EtaoPcP__7->SetBinContent(33,171);
   EtaoPcP__7->SetBinContent(34,179);
   EtaoPcP__7->SetBinContent(35,181);
   EtaoPcP__7->SetBinContent(36,194);
   EtaoPcP__7->SetBinContent(37,212);
   EtaoPcP__7->SetBinContent(38,221);
   EtaoPcP__7->SetBinContent(39,217);
   EtaoPcP__7->SetBinContent(40,221);
   EtaoPcP__7->SetBinContent(41,232);
   EtaoPcP__7->SetBinContent(42,256);
   EtaoPcP__7->SetBinContent(43,271);
   EtaoPcP__7->SetBinContent(44,234);
   EtaoPcP__7->SetBinContent(45,245);
   EtaoPcP__7->SetBinContent(46,292);
   EtaoPcP__7->SetBinContent(47,239);
   EtaoPcP__7->SetBinContent(48,264);
   EtaoPcP__7->SetBinContent(49,273);
   EtaoPcP__7->SetBinContent(50,305);
   EtaoPcP__7->SetBinContent(51,274);
   EtaoPcP__7->SetBinContent(52,298);
   EtaoPcP__7->SetBinContent(53,276);
   EtaoPcP__7->SetBinContent(54,238);
   EtaoPcP__7->SetBinContent(55,308);
   EtaoPcP__7->SetBinContent(56,236);
   EtaoPcP__7->SetBinContent(57,246);
   EtaoPcP__7->SetBinContent(58,274);
   EtaoPcP__7->SetBinContent(59,251);
   EtaoPcP__7->SetBinContent(60,250);
   EtaoPcP__7->SetBinContent(61,214);
   EtaoPcP__7->SetBinContent(62,241);
   EtaoPcP__7->SetBinContent(63,217);
   EtaoPcP__7->SetBinContent(64,215);
   EtaoPcP__7->SetBinContent(65,207);
   EtaoPcP__7->SetBinContent(66,181);
   EtaoPcP__7->SetBinContent(67,171);
   EtaoPcP__7->SetBinContent(68,202);
   EtaoPcP__7->SetBinContent(69,174);
   EtaoPcP__7->SetBinContent(70,164);
   EtaoPcP__7->SetBinContent(71,166);
   EtaoPcP__7->SetBinContent(72,170);
   EtaoPcP__7->SetBinContent(73,126);
   EtaoPcP__7->SetBinContent(74,143);
   EtaoPcP__7->SetBinContent(75,105);
   EtaoPcP__7->SetBinContent(76,81);
   EtaoPcP__7->SetBinContent(77,83);
   EtaoPcP__7->SetBinContent(78,113);
   EtaoPcP__7->SetBinContent(79,80);
   EtaoPcP__7->SetBinContent(80,100);
   EtaoPcP__7->SetBinContent(81,84);
   EtaoPcP__7->SetBinContent(82,80);
   EtaoPcP__7->SetBinContent(83,80);
   EtaoPcP__7->SetBinContent(84,75);
   EtaoPcP__7->SetBinContent(85,61);
   EtaoPcP__7->SetBinContent(86,51);
   EtaoPcP__7->SetBinContent(87,46);
   EtaoPcP__7->SetBinContent(88,40);
   EtaoPcP__7->SetBinContent(89,40);
   EtaoPcP__7->SetBinContent(90,30);
   EtaoPcP__7->SetBinContent(91,42);
   EtaoPcP__7->SetBinContent(92,29);
   EtaoPcP__7->SetBinContent(93,7);
   EtaoPcP__7->SetEntries(12717);
   EtaoPcP__7->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   EtaoPcP__7->SetLineColor(ci);
   EtaoPcP__7->GetXaxis()->SetRange(1,100);
   EtaoPcP__7->GetXaxis()->SetLabelFont(42);
   EtaoPcP__7->GetXaxis()->SetTitleOffset(1);
   EtaoPcP__7->GetXaxis()->SetTitleFont(42);
   EtaoPcP__7->GetYaxis()->SetLabelFont(42);
   EtaoPcP__7->GetYaxis()->SetTitleFont(42);
   EtaoPcP__7->GetZaxis()->SetLabelFont(42);
   EtaoPcP__7->GetZaxis()->SetTitleOffset(1);
   EtaoPcP__7->GetZaxis()->SetTitleFont(42);
   EtaoPcP__7->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return EtaoPcP__7;
}


TH1F* TrigMatched_Taus_HLTptfl_Phi()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 03:22:25 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *PhioPcP__8 = new TH1F("PhioPcP__8","TrigMatched_Taus_HLTptfl.Phi()",100,-3.7,3.7);
   PhioPcP__8->SetBinContent(8,58);
   PhioPcP__8->SetBinContent(9,166);
   PhioPcP__8->SetBinContent(10,183);
   PhioPcP__8->SetBinContent(11,147);
   PhioPcP__8->SetBinContent(12,127);
   PhioPcP__8->SetBinContent(13,148);
   PhioPcP__8->SetBinContent(14,156);
   PhioPcP__8->SetBinContent(15,162);
   PhioPcP__8->SetBinContent(16,132);
   PhioPcP__8->SetBinContent(17,171);
   PhioPcP__8->SetBinContent(18,171);
   PhioPcP__8->SetBinContent(19,145);
   PhioPcP__8->SetBinContent(20,141);
   PhioPcP__8->SetBinContent(21,156);
   PhioPcP__8->SetBinContent(22,155);
   PhioPcP__8->SetBinContent(23,162);
   PhioPcP__8->SetBinContent(24,137);
   PhioPcP__8->SetBinContent(25,164);
   PhioPcP__8->SetBinContent(26,171);
   PhioPcP__8->SetBinContent(27,152);
   PhioPcP__8->SetBinContent(28,136);
   PhioPcP__8->SetBinContent(29,149);
   PhioPcP__8->SetBinContent(30,167);
   PhioPcP__8->SetBinContent(31,148);
   PhioPcP__8->SetBinContent(32,131);
   PhioPcP__8->SetBinContent(33,152);
   PhioPcP__8->SetBinContent(34,144);
   PhioPcP__8->SetBinContent(35,151);
   PhioPcP__8->SetBinContent(36,142);
   PhioPcP__8->SetBinContent(37,140);
   PhioPcP__8->SetBinContent(38,173);
   PhioPcP__8->SetBinContent(39,154);
   PhioPcP__8->SetBinContent(40,113);
   PhioPcP__8->SetBinContent(41,152);
   PhioPcP__8->SetBinContent(42,159);
   PhioPcP__8->SetBinContent(43,152);
   PhioPcP__8->SetBinContent(44,130);
   PhioPcP__8->SetBinContent(45,142);
   PhioPcP__8->SetBinContent(46,141);
   PhioPcP__8->SetBinContent(47,188);
   PhioPcP__8->SetBinContent(48,122);
   PhioPcP__8->SetBinContent(49,131);
   PhioPcP__8->SetBinContent(50,151);
   PhioPcP__8->SetBinContent(51,144);
   PhioPcP__8->SetBinContent(52,157);
   PhioPcP__8->SetBinContent(53,171);
   PhioPcP__8->SetBinContent(54,152);
   PhioPcP__8->SetBinContent(55,162);
   PhioPcP__8->SetBinContent(56,130);
   PhioPcP__8->SetBinContent(57,114);
   PhioPcP__8->SetBinContent(58,176);
   PhioPcP__8->SetBinContent(59,170);
   PhioPcP__8->SetBinContent(60,138);
   PhioPcP__8->SetBinContent(61,146);
   PhioPcP__8->SetBinContent(62,150);
   PhioPcP__8->SetBinContent(63,145);
   PhioPcP__8->SetBinContent(64,149);
   PhioPcP__8->SetBinContent(65,134);
   PhioPcP__8->SetBinContent(66,169);
   PhioPcP__8->SetBinContent(67,185);
   PhioPcP__8->SetBinContent(68,151);
   PhioPcP__8->SetBinContent(69,135);
   PhioPcP__8->SetBinContent(70,146);
   PhioPcP__8->SetBinContent(71,164);
   PhioPcP__8->SetBinContent(72,161);
   PhioPcP__8->SetBinContent(73,147);
   PhioPcP__8->SetBinContent(74,145);
   PhioPcP__8->SetBinContent(75,153);
   PhioPcP__8->SetBinContent(76,148);
   PhioPcP__8->SetBinContent(77,115);
   PhioPcP__8->SetBinContent(78,158);
   PhioPcP__8->SetBinContent(79,136);
   PhioPcP__8->SetBinContent(80,145);
   PhioPcP__8->SetBinContent(81,153);
   PhioPcP__8->SetBinContent(82,146);
   PhioPcP__8->SetBinContent(83,156);
   PhioPcP__8->SetBinContent(84,169);
   PhioPcP__8->SetBinContent(85,149);
   PhioPcP__8->SetBinContent(86,131);
   PhioPcP__8->SetBinContent(87,147);
   PhioPcP__8->SetBinContent(88,143);
   PhioPcP__8->SetBinContent(89,138);
   PhioPcP__8->SetBinContent(90,130);
   PhioPcP__8->SetBinContent(91,160);
   PhioPcP__8->SetBinContent(92,160);
   PhioPcP__8->SetBinContent(93,67);
   PhioPcP__8->SetEntries(12717);
   PhioPcP__8->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   PhioPcP__8->SetLineColor(ci);
   PhioPcP__8->GetXaxis()->SetRange(1,100);
   PhioPcP__8->GetXaxis()->SetLabelFont(42);
   PhioPcP__8->GetXaxis()->SetTitleOffset(1);
   PhioPcP__8->GetXaxis()->SetTitleFont(42);
   PhioPcP__8->GetYaxis()->SetLabelFont(42);
   PhioPcP__8->GetYaxis()->SetTitleFont(42);
   PhioPcP__8->GetZaxis()->SetLabelFont(42);
   PhioPcP__8->GetZaxis()->SetTitleOffset(1);
   PhioPcP__8->GetZaxis()->SetTitleFont(42);
   PhioPcP__8->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return PhioPcP__8;
}

TH1F* TrigMatched_prong_HLTptfl()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 03:23:25 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *TrigMatched_prong_HLTptfl__9 = new TH1F("TrigMatched_prong_HLTptfl__9","TrigMatched_prong_HLTptfl.TrigMatched_prong_HLTptfl",24,0,24);
   TrigMatched_prong_HLTptfl__9->SetBinContent(1,163);
   TrigMatched_prong_HLTptfl__9->SetBinContent(2,8449);
   TrigMatched_prong_HLTptfl__9->SetBinContent(3,1595);
   TrigMatched_prong_HLTptfl__9->SetBinContent(4,2481);
   TrigMatched_prong_HLTptfl__9->SetBinContent(5,7);
   TrigMatched_prong_HLTptfl__9->SetBinContent(6,2);
   TrigMatched_prong_HLTptfl__9->SetBinContent(7,1);
   TrigMatched_prong_HLTptfl__9->SetBinContent(8,4);
   TrigMatched_prong_HLTptfl__9->SetBinContent(9,3);
   TrigMatched_prong_HLTptfl__9->SetBinContent(11,3);
   TrigMatched_prong_HLTptfl__9->SetBinContent(14,1);
   TrigMatched_prong_HLTptfl__9->SetBinContent(16,3);
   TrigMatched_prong_HLTptfl__9->SetBinContent(18,3);
   TrigMatched_prong_HLTptfl__9->SetBinContent(23,2);
   TrigMatched_prong_HLTptfl__9->SetEntries(12717);
   TrigMatched_prong_HLTptfl__9->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   TrigMatched_prong_HLTptfl__9->SetLineColor(ci);
   TrigMatched_prong_HLTptfl__9->GetXaxis()->SetRange(1,100);
   TrigMatched_prong_HLTptfl__9->GetXaxis()->SetLabelFont(42);
   TrigMatched_prong_HLTptfl__9->GetXaxis()->SetTitleOffset(1);
   TrigMatched_prong_HLTptfl__9->GetXaxis()->SetTitleFont(42);
   TrigMatched_prong_HLTptfl__9->GetYaxis()->SetLabelFont(42);
   TrigMatched_prong_HLTptfl__9->GetYaxis()->SetTitleFont(42);
   TrigMatched_prong_HLTptfl__9->GetZaxis()->SetLabelFont(42);
   TrigMatched_prong_HLTptfl__9->GetZaxis()->SetTitleOffset(1);
   TrigMatched_prong_HLTptfl__9->GetZaxis()->SetTitleFont(42);
   TrigMatched_prong_HLTptfl__9->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
   return TrigMatched_prong_HLTptfl__9;
}


TH1F* TrigMatched_rnn_HLTptfl()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Mon May 23 03:24:44 2022) by ROOT version 6.26/02
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",0,0,4,28);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *TrigMatched_rnn_HLTptfl__10 = new TH1F("TrigMatched_rnn_HLTptfl__10","TrigMatched_rnn_HLTptfl.TrigMatched_rnn_HLTptfl",100,0,1.08);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(1,22);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(2,5);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(3,9);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(4,160);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(5,167);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(6,186);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(7,173);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(8,150);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(9,166);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(10,193);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(11,170);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(12,162);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(13,186);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(14,224);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(15,247);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(16,249);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(17,217);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(18,194);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(19,234);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(20,213);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(21,198);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(22,211);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(23,230);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(24,211);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(25,197);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(26,192);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(27,192);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(28,163);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(29,187);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(30,179);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(31,158);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(32,149);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(33,150);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(34,174);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(35,155);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(36,144);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(37,131);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(38,116);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(39,112);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(40,98);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(41,127);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(42,112);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(43,107);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(44,112);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(45,106);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(46,87);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(47,122);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(48,95);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(49,86);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(50,76);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(51,112);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(52,81);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(53,88);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(54,80);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(55,82);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(56,94);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(57,86);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(58,87);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(59,86);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(60,89);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(61,78);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(62,74);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(63,89);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(64,92);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(65,96);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(66,92);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(67,96);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(68,89);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(69,98);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(70,94);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(71,98);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(72,93);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(73,103);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(74,100);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(75,112);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(76,128);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(77,104);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(78,138);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(79,111);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(80,143);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(81,131);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(82,136);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(83,149);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(84,126);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(85,156);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(86,158);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(87,143);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(88,165);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(89,161);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(90,180);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(91,201);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(92,393);
   TrigMatched_rnn_HLTptfl__10->SetBinContent(93,1);
   TrigMatched_rnn_HLTptfl__10->SetEntries(12717);
   TrigMatched_rnn_HLTptfl__10->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   TrigMatched_rnn_HLTptfl__10->SetLineColor(ci);
   TrigMatched_rnn_HLTptfl__10->GetXaxis()->SetRange(1,100);
   TrigMatched_rnn_HLTptfl__10->GetXaxis()->SetLabelFont(42);
   TrigMatched_rnn_HLTptfl__10->GetXaxis()->SetTitleOffset(1);
   TrigMatched_rnn_HLTptfl__10->GetXaxis()->SetTitleFont(42);
   TrigMatched_rnn_HLTptfl__10->GetYaxis()->SetLabelFont(42);
   TrigMatched_rnn_HLTptfl__10->GetYaxis()->SetTitleFont(42);
   TrigMatched_rnn_HLTptfl__10->GetZaxis()->SetLabelFont(42);
   TrigMatched_rnn_HLTptfl__10->GetZaxis()->SetTitleOffset(1);
   TrigMatched_rnn_HLTptfl__10->GetZaxis()->SetTitleFont(42);
   TrigMatched_rnn_HLTptfl__10->Draw("");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);

   return TrigMatched_rnn_HLTptfl__10;
}


vector<TH1F*> createHistogram_Offline_Matched_Taus(){
   vector<TH1F*> a;
   a.push_back(Offline_Matched_Taus_Pt());
   a.push_back(Offline_Matched_Taus_Eta());
   a.push_back(Offline_Matched_Taus_Phi());
   a.push_back(Offline_Matched_Taus_Prong());
   a.push_back(Offline_Matched_Taus_RNN());
   return a;
}

vector<TH1F*> createHistogram_TrigMatched_Taus_HLTetafl(){
   vector<TH1F*> a;

   a.push_back(TrigMatched_Taus_HLTetafl_Pt());
   a.push_back(TrigMatched_Taus_HLTetafl_Eta());
   a.push_back(TrigMatched_Taus_HLTetafl_Phi());
   a.push_back(TrigMatched_prong_HLTetafl());
   a.push_back(TrigMatched_rnn_HLTetafl());
   return a;
}

vector<TH1F*> createHistogram_TrigMatched_Taus_HLTptfl(){
   vector<TH1F*> a;
   a.push_back(TrigMatched_Taus_HLTptfl_Pt());
   a.push_back(TrigMatched_Taus_HLTptfl_Eta());
   a.push_back(TrigMatched_Taus_HLTptfl_Phi());
   a.push_back(TrigMatched_prong_HLTptfl());
   a.push_back(TrigMatched_rnn_HLTptfl());
   return a;
}

void two_cut(vector<THStack*>& hs_list, const char* name,const char* blue_red ,TH1F * h1, TH1F* h2){
    std::string hs = "hs_";
    hs+=name;
    std::string cut = " Cut";
    std::string cut1 = name;
    cut1 = cut1+ blue_red;
    cut1 = cut1+ cut;
    THStack* hs_tau = new THStack(hs.c_str(), cut1.c_str());
    std::cout<<hs.c_str()<<cut1.c_str()<<std::endl;
    h1->SetLineColor(kBlue);
    h2->SetLineColor(kRed);
    hs_tau->Add(h1);
    hs_tau->Add(h2);
    hs_list.push_back(hs_tau);
}

void r22_Passed(){
  vector<TH1F*> hl_Offline_Matched_Taus;
  vector<TH1F*> hl_TrigMatched_Taus_HLTetafl;
  vector<TH1F*> hl_TrigMatched_Taus_HLTptfl;
  hl_Offline_Matched_Taus = createHistogram_Offline_Matched_Taus();
  hl_TrigMatched_Taus_HLTetafl = createHistogram_TrigMatched_Taus_HLTetafl();
  hl_TrigMatched_Taus_HLTptfl = createHistogram_TrigMatched_Taus_HLTptfl();
  const char* a [5] = {"Pt", "Eta", "Phi", "Prong", "rnn"};

  TCanvas *c1 = new TCanvas();
  vector <THStack*> hs_list;
  for(int i = 0; i<5; i++){
    two_cut(hs_list, 
    a[i], "Eta(Blue) vs. Pt(Red)",
    hl_TrigMatched_Taus_HLTetafl[i],
    hl_TrigMatched_Taus_HLTptfl[i]);
  }

  std::string pdf_tau_s = "tau_r22_Passed.pdf(";
  std::string pdf_tau = "tau_r22_Passed.pdf";
  std::string pdf_tau_e = "tau_r22_Passed.pdf)";

  hs_list[0]->Draw("nostack");
  c1->Print(pdf_tau_s.c_str(), "pdf");
  for(int i = 1; i< (hs_list.size()-1); i++){
      hs_list[i]->Draw("nostack");
      c1->Print(pdf_tau.c_str(),"pdf");
  }
  hs_list[hs_list.size()-1]->Draw("nostack");
  c1->Print(pdf_tau_e.c_str(), "pdf");
}

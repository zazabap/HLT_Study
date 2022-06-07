// Author: Shiwen An
// Date: 2022/05/19
// Purpose: To create the code block for 
//    repetition purpose

void two_cut(vector<THStack*>& hs_list, const char* name,
TFile*r1, TFile*r2, TH1F * h1, TH1F* h2){
    
    std::string plot = "analysis/";
    plot = plot+name;
    r1->GetObject(name, h1);
    r2->GetObject(name, h2);
    std::string hs = "hs_";
    hs+=name;
    std::string cut = " Cut";
    std::string cut1 = name + cut;
    THStack* hs_tau = new THStack(hs.c_str(), cut1.c_str());
    std::cout<<hs.c_str()<<cut1.c_str()<<std::endl;
    h1->SetLineColor(kBlue);
    h2->SetLineColor(kRed);
    hs_tau->Add(h1);
    hs_tau->Add(h2);
    hs_list.push_back(hs_tau);
}

void tree_two_cut(vector<THStack*>& hs_list, const char* name,
TFile*r1, TFile*r2, TH1F * h1, TH1F* h2){
    
    std::string plot = "analysis/";
    plot = plot+name;
    r1->GetObject(name, h1);
    r2->GetObject(name, h2);

    // h1= t1->GetBranch(name)->GetEntries();
    // h2 = t2->GetBranch(name)->GetEntries();

    std::string hs = "hs_";
    hs+=name;
    std::string cut = " Cut";
    std::string cut1 = name + cut;
    THStack* hs_tau = new THStack(hs.c_str(), cut1.c_str());
    std::cout<<hs.c_str()<<cut1.c_str()<<std::endl;
    h1->SetLineColor(kBlue);
    h2->SetLineColor(kRed);
    hs_tau->Add(h1);
    hs_tau->Add(h2);
    hs_list.push_back(hs_tau);
}

void three_cut(vector<THStack*>& hs_list, const char* name,
TFile*r1, TFile*r2, TFile*r3, TH1F * h1, TH1F* h2, TH1F * h3){
    r1->GetObject(name, h1);
    r2->GetObject(name, h2);
    r3->GetObject(name, h3);

    std::string hs = "hs_";
    hs+=name;
    std::string cut = " Cut";
    std::string cut1 = name + cut;
    THStack* hs_tau = new THStack(hs.c_str(), cut1.c_str());

    h1->SetLineColor(kBlack);
    h2->SetLineColor(kBlue);
    h3->SetLineColor(kRed);

    hs_tau->Add(h1);
    hs_tau->Add(h2);
    hs_tau->Add(h3);

    hs_list.push_back(hs_tau);
}

void crosscheck(){


//    TCanvas *c1 = new TCanvas();
//    vector <THStack*> hs_list;
//    std::string pdf_tau_s = "tau_a.pdf(";
//    std::string pdf_tau = "tau_a.pdf";
//    std::string pdf_tau_e = "tau_a.pdf)";

//    TH1F* h1 ;
//    TH1F* h2 ;

TFile* r1 = TFile::Open("r22_Passed.root");
TTree* t1 = (TTree*) r1->Get("analysis");

vector<unsigned long>* TrigMatched_prong_HLTptfl;
vector<double> *  TrigMatched_rnn_HLTptfl;
vector<TLorentzVector> * vec;
t1->SetBranchAddress("TrigMatched_prong_HLTptfl", &TrigMatched_prong_HLTptfl );
t1->SetBranchAddress("TrigMatched_rnn_HLTptfl", &TrigMatched_rnn_HLTptfl);

t1->SetBranchAddress("TrigMatched_Taus_HLTptfl", &vec);


//for(int i = 0; i< sizeof(TrigMatched_prong_HLTptfl); i++) std::cout<<(*TrigMatched_prong_HLTptfl)[i]<<std::endl;

//for(int i = 0; i< sizeof(TrigMatched_rnn_HLTptfl); i++) std::cout<<(*TrigMatched_rnn_HLTptfl)[i]<<std::endl;

for(int i = 0; i< sizeof(vec); i++) std::cout<<(*vec)[i].Phi()<<std::endl;
// for (Int_t i = 0; i<nentries; i++) {
//    t1->GetEntry(i);
//    //the object event has been filled at this point
// }
   
LAr detect two charge signal in LAr Muon region. 
Maybe is my own problem not understand the TGC enough. 
How to Seprate the crosstalk of the event and the real two partilces case? 
//    TFile* r2 = TFile::Open("r22_PassedFailed.root");
//    TTree* t2 = (TTree*) r2->Get("analysis");

//    //TFile* r3 = TFile::Open("Tau0_Passed.root");
//    //TFile* r4 = Tfile::Open("Tau0_PassedFailed.root");
//    std::cout<<"Get into individual plot"<<std::endl;
//    tree_two_cut(hs_list, "HLT_ETA25_Tau0", t1, t2, h1, h2);

//    hs_list[0]->Draw("nostack");
//    c1->Print(pdf_tau_s.c_str(), "pdf");
//    for(int i = 1; i< (hs_list.size()-1); i++){
//       hs_list[i]->Draw("nostack");
//       c1->Print(pdf_tau.c_str(),"pdf");
//    }
//    hs_list[hs_list.size()-1]->Draw("nostack");
//    c1->Print(pdf_tau_e.c_str(), "pdf");
   
}
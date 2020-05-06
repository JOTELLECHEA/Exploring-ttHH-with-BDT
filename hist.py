# Written By : Jonathan O. Tellechea
# Adviser    : Mike Hance, Phd
# Research   : ttHH - All Histogram
# 12scription: Histogram of ttHH from pg.8 in http://cdsweb.cern.ch/record/2220969/files/ATL-PHYS-PUB-2016-023.pdf
#------------------------------------------------------------------------------#
import ROOT
import array as arr
from tabulate import tabulate
#------------------------------ root file -------------------------------------#
g = ROOT.TFile('all_hist.root')
#---------------------------- load Histogram ----------------------------------#
ttHH0  = g.Get('ttHH0')
ttHH1  = g.Get('ttHH1')
ttHH2  = g.Get('ttHH2')
ttHH3  = g.Get('ttHH3')
ttHH4  = g.Get('ttHH4')
ttHH5  = g.Get('ttHH5')
ttHH6  = g.Get('ttHH6')
ttHH7  = g.Get('ttHH7')
ttHH8  = g.Get('ttHH8')
ttHH9  = g.Get('ttHH9')
ttHH10 = g.Get('ttHH10')
ttHH11 = g.Get('ttHH11')
ttHH12 = g.Get('ttHH12')
ttHH13 = g.Get('ttHH13')
ttHH14 = g.Get('ttHH14')
ttHH15 = g.Get('ttHH15')
ttHH16 = g.Get('ttHH16')
ttHH17 = g.Get('ttHH17')
ttbb0  = g.Get('ttbb0')
ttbb1  = g.Get('ttbb1')
ttbb2  = g.Get('ttbb2')
ttbb3  = g.Get('ttbb3')
ttbb4  = g.Get('ttbb4')
ttbb5  = g.Get('ttbb5')
ttbb6  = g.Get('ttbb6')
ttbb7  = g.Get('ttbb7')
ttbb8  = g.Get('ttbb8')
ttbb9  = g.Get('ttbb9')
ttbb10 = g.Get('ttbb10')
ttbb11 = g.Get('ttbb11')
ttbb12 = g.Get('ttbb12')
ttbb13 = g.Get('ttbb13')
ttbb14 = g.Get('ttbb14')
ttbb15 = g.Get('ttbb15')
ttbb16 = g.Get('ttbb16')
ttbb17 = g.Get('ttbb17')
ttH0  = g.Get('ttH0')
ttH1  = g.Get('ttH1')
ttH2  = g.Get('ttH2')
ttH3  = g.Get('ttH3')
ttH4  = g.Get('ttH4')
ttH5  = g.Get('ttH5')
ttH6  = g.Get('ttH6')
ttH7  = g.Get('ttH7')
ttH8  = g.Get('ttH8')
ttH9  = g.Get('ttH9')
ttH10 = g.Get('ttH10')
ttH11 = g.Get('ttH11')
ttH12 = g.Get('ttH12')
ttH13 = g.Get('ttH13')
ttH14 = g.Get('ttH14')
ttH15 = g.Get('ttH15')
ttH16 = g.Get('ttH16')
ttH17 = g.Get('ttH17')
ttZ0  = g.Get('ttZ0')
ttZ1  = g.Get('ttZ1')
ttZ2  = g.Get('ttZ2')
ttZ3  = g.Get('ttZ3')
ttZ4  = g.Get('ttZ4')
ttZ5  = g.Get('ttZ5')
ttZ6  = g.Get('ttZ6')
ttZ7  = g.Get('ttZ7')
ttZ8  = g.Get('ttZ8')
ttZ9  = g.Get('ttZ9')
ttZ10 = g.Get('ttZ10')
ttZ11 = g.Get('ttZ11')
ttZ12 = g.Get('ttZ12')
ttZ13 = g.Get('ttZ13')
ttZ14 = g.Get('ttZ14')
ttZ15 = g.Get('ttZ15')
ttZ16 = g.Get('ttZ16')
ttZ17 = g.Get('ttZ17')
#---------------------------Functions------------------------------------------#
def HH0(x):return int(ttHH0.GetBinContent(x))
def H0(x):return int(ttH0.GetBinContent(x))
def Z0(x):return int(ttZ0.GetBinContent(x))
def bb0(x):return int(ttbb0.GetBinContent(x))
#---------------------------table/values --------------------------------------#
xxHH = ['ttHH', HH0(1),HH0(2),HH0(3),HH0(4),HH0(5),HH0(6),HH0(7)]
xxH  = ['ttH',  H0(1),H0(2),H0(3),H0(4),H0(5),H0(6),H0(7)]
xxZ  = ['ttZ',  Z0(1),Z0(2),Z0(3),Z0(4),Z0(5),Z0(6),Z0(7)]
xxbb = ['ttbb', bb0(1),bb0(2),bb0(3),bb0(4),bb0(5),bb0(6),bb0(7)]
t1 = HH0(1) + H0(1) + Z0(1) + bb0(1)
t2 = HH0(2) + H0(2) + Z0(2) + bb0(2)
t3 = HH0(3) + H0(3) + Z0(3) + bb0(3)
t4 = HH0(4) + H0(4) + Z0(4) + bb0(4)
t5 = HH0(5) + H0(5) + Z0(5) + bb0(5)
t6 = HH0(6) + H0(6) + Z0(6) + bb0(6)
t7 = HH0(7) + H0(7) + Z0(7) + bb0(7)
total = ['Total background',t1,t2,t3,t4,t5,t6,t7]
headers1=['Sample          ','No cuts','Trigger','One lepton',' >= 7 jets','>= 5 b-tags',' n(bi,bj)','>=6b-tags']
headerst=['                ','       ','       ','          ','          ','           ','         ','         ']
#-----------------------------TLegend------------------------------------------#
leg = ROOT.TLegend(0.69,0.69,0.89,0.89)
leg.SetLineColor(ROOT.kWhite)
leg.AddEntry(ttHH1,'ttHH')
leg.AddEntry(ttH1,'ttH')
leg.AddEntry(ttZ1,'ttZ')
leg.AddEntry(ttbb1,'ttbb')
table = False
if(table == True):print(tabulate([xxHH,xxH,xxZ,xxbb,total],headers1, tablefmt='pipe'))
latex = True
if(latex == True):print(tabulate([xxHH,xxH,xxZ,xxbb,total],headers1, tablefmt='latex'))
thesisPlots = True
if (thesisPlots == True):
    c00 = ROOT.TCanvas('c00','Jet multiplicity',500,500)
    c01 = ROOT.TCanvas('c01','N b-tagged jets',500,500)
    c02 = ROOT.TCanvas('c02','< #eta(b_{i},b_{j}) >',500,500)
    c03 = ROOT.TCanvas('c03','M_{bb};M_{bb}',500,500)
    c04 = ROOT.TCanvas('c04','Centrality',500,500)
    c05 = ROOT.TCanvas('c05','H_{B};H_{B}',500,500)
    c02.cd()##################################### Seperation between two b-tag jets.
    ttHH1.SetLineColor(ROOT.kRed)
    ttHH1.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH1.SetStats(0)
    ttHH1.Scale(1/(ttHH1.Integral()))
    ttHH1.Draw('HIST SAME')
    ttHH1.SetAxisRange(0.,.36,'Y')
    ttH1.SetLineColor(ROOT.kAzure)
    ttH1.Scale(1/(ttH1.Integral()))
    ttH1.Draw('HIST SAME')
    ttZ1.SetLineColor(ROOT.kMagenta)
    ttZ1.Scale(1/(ttZ1.Integral()))
    ttZ1.Draw('HIST SAME')
    ttbb1.SetLineColor(ROOT.kGreen+2)
    ttbb1.Scale(1/(ttbb1.Integral()))
    ttbb1.Draw('HIST SAME')
    leg.Draw()
    c03.cd()################################################### Higgs canidate mass.
    ttHH2.SetLineColor(ROOT.kRed)
    ttHH2.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH2.SetStats(0)
    ttHH2.Scale(1/(ttHH2.Integral()))
    ttHH2.Draw('HIST SAME')
    ttHH2.SetAxisRange(0.,.405,'Y')
    ttH2.SetLineColor(ROOT.kAzure)
    ttH2.Scale(1/(ttH2.Integral()))
    ttH2.Draw('HIST SAME')
    ttZ2.SetLineColor(ROOT.kMagenta)
    ttZ2.Scale(1/(ttZ2.Integral()))
    ttZ2.Draw('HIST SAME')
    ttbb2.SetLineColor(ROOT.kGreen+2)
    ttbb2.Scale(1/(ttbb2.Integral()))
    ttbb2.Draw('HIST SAME')
    leg.Draw()
    c04.cd()############################################################ Centrality.
    ttHH3.SetLineColor(ROOT.kRed)
    ttHH3.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH3.SetStats(0)
    ttHH3.Scale(1/(ttHH3.Integral()))
    ttHH3.SetAxisRange(0.,.27,'Y')
    ttHH3.Draw('HIST SAME')
    ttH3.SetLineColor(ROOT.kAzure)
    ttH3.Scale(1/(ttH3.Integral()))
    ttH3.Draw('HIST SAME')
    ttZ3.SetLineColor(ROOT.kMagenta)
    ttZ3.Scale(1/(ttZ3.Integral()))
    ttZ3.Draw('HIST SAME')
    ttbb3.SetLineColor(ROOT.kGreen+2)
    ttbb3.Scale(1/(ttbb3.Integral()))
    ttbb3.Draw('HIST SAME')
    leg.Draw()
    c05.cd()################################################################### H_B.
    ttHH4.SetLineColor(ROOT.kRed)
    ttHH4.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH4.SetStats(0)
    ttHH4.Scale(1/(ttHH4.Integral()))
    ttHH4.Draw('HIST SAME')
    ttHH4.SetAxisRange(0.,.51,'Y')
    ttH4.SetLineColor(ROOT.kAzure)
    ttH4.Scale(1/(ttH4.Integral()))
    ttH4.Draw('HIST SAME')
    ttZ4.SetLineColor(ROOT.kMagenta)
    ttZ4.Scale(1/(ttZ4.Integral()))
    ttZ4.Draw('HIST SAME')
    ttbb4.SetLineColor(ROOT.kGreen+2)
    ttbb4.Scale(1/(ttbb4.Integral()))
    ttbb4.Draw('HIST SAME')
    leg.Draw()
    c00.cd()####################################################### Jet muliplicity.
    ttHH5.SetLineColor(ROOT.kRed)
    ttHH5.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH5.SetStats(0)
    ttHH5.Scale(1/(ttHH5.Integral()))
    ttHH5.SetAxisRange(0.,.3,'Y')
    ttHH5.Draw('HIST SAME')
    ttH5.SetLineColor(ROOT.kAzure)
    ttH5.Scale(1/(ttH5.Integral()))
    ttH5.Draw('HIST SAME')
    ttZ5.SetLineColor(ROOT.kMagenta)
    ttZ5.Scale(1/(ttZ5.Integral()))
    ttZ5.Draw('HIST SAME')
    ttbb5.SetLineColor(ROOT.kGreen+2)
    ttbb5.Scale(1/(ttbb5.Integral()))
    ttbb5.Draw('HIST SAME')
    leg.Draw()
    c01.cd()############################################### Number of b-tagged jets.
    ttHH6.SetLineColor(ROOT.kRed)
    ttHH6.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH6.SetStats(0)
    ttHH6.Scale(1/(ttHH6.Integral()))
    ttHH6.SetAxisRange(0.,.40,'Y')
    ttHH6.Draw('HIST SAME')
    ttH6.SetLineColor(ROOT.kAzure)
    ttH6.Scale(1/(ttH6.Integral()))
    ttH6.Draw('HIST SAME')
    ttZ6.SetLineColor(ROOT.kMagenta)
    ttZ6.Scale(1/(ttZ6.Integral()))
    ttZ6.Draw('HIST SAME')
    ttbb6.SetLineColor(ROOT.kGreen+2)
    ttbb6.Scale(1/(ttbb6.Integral()))
    ttbb6.Draw('HIST SAME')
    leg.Draw()



fullCanvasPresentation = False
if (fullCanvasPresentation == True):
    #---------------------------Canvas and THStack---------------------------------#
    c1 = ROOT.TCanvas('c1','Canvas 1',710,100,1000,500)
    c2 = ROOT.TCanvas('c2','Canvas 2',710,100,1000,500)
    c3 = ROOT.TCanvas('c3','Canvas 3',710,100,1000,500)
    cf = ROOT.THStack('cf','CutFlow;Cuts;Events')
    #-----------------------------bin labels---------------------------------------#
    for i in xrange(1,8):
        ttHH0.GetXaxis().SetBinLabel(i,headers1[i])
        ttH0.GetXaxis().SetBinLabel(i,headers1[i])
        ttZ0.GetXaxis().SetBinLabel(i,headers1[i])
        ttbb0.GetXaxis().SetBinLabel(i,headers1[i])
    #------------------------------------------------------------------------------#
    c1.Divide(3,2,0.01,0.01,0)
    c2.Divide(3,2,0.01,0.01,0)
    c3.Divide(3,2,0.01,0.01,0)

    c1.cd(1)##################################### Seperation between two b-tag jets.
    ttHH1.SetLineColor(ROOT.kRed)
    ttHH1.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH1.SetStats(0)
    ttHH1.Scale(1/(ttHH1.Integral()))
    ttHH1.Draw('HIST SAME')
    ttHH1.SetAxisRange(0.,.36,'Y')
    ttH1.SetLineColor(ROOT.kAzure)
    ttH1.Scale(1/(ttH1.Integral()))
    ttH1.Draw('HIST SAME')
    ttZ1.SetLineColor(ROOT.kMagenta)
    ttZ1.Scale(1/(ttZ1.Integral()))
    ttZ1.Draw('HIST SAME')
    ttbb1.SetLineColor(ROOT.kGreen+2)
    ttbb1.Scale(1/(ttbb1.Integral()))
    ttbb1.Draw('HIST SAME')
    leg.Draw()


    c1.cd(2)################################################### Higgs canidate mass.
    ttHH2.SetLineColor(ROOT.kRed)
    ttHH2.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH2.SetStats(0)
    ttHH2.Scale(1/(ttHH2.Integral()))
    ttHH2.Draw('HIST SAME')
    ttHH2.SetAxisRange(0.,.405,'Y')
    ttH2.SetLineColor(ROOT.kAzure)
    ttH2.Scale(1/(ttH2.Integral()))
    ttH2.Draw('HIST SAME')
    ttZ2.SetLineColor(ROOT.kMagenta)
    ttZ2.Scale(1/(ttZ2.Integral()))
    ttZ2.Draw('HIST SAME')
    ttbb2.SetLineColor(ROOT.kGreen+2)
    ttbb2.Scale(1/(ttbb2.Integral()))
    ttbb2.Draw('HIST SAME')
    leg.Draw()

    c1.cd(3)############################################################ Centrality.
    ttHH3.SetLineColor(ROOT.kRed)
    ttHH3.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH3.SetStats(0)
    ttHH3.Scale(1/(ttHH3.Integral()))
    ttHH3.SetAxisRange(0.,.27,'Y')
    ttHH3.Draw('HIST SAME')
    ttH3.SetLineColor(ROOT.kAzure)
    ttH3.Scale(1/(ttH3.Integral()))
    ttH3.Draw('HIST SAME')
    ttZ3.SetLineColor(ROOT.kMagenta)
    ttZ3.Scale(1/(ttZ3.Integral()))
    ttZ3.Draw('HIST SAME')
    ttbb3.SetLineColor(ROOT.kGreen+2)
    ttbb3.Scale(1/(ttbb3.Integral()))
    ttbb3.Draw('HIST SAME')
    leg.Draw()

    c1.cd(4)################################################################### H_B.
    ttHH4.SetLineColor(ROOT.kRed)
    ttHH4.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH4.SetStats(0)
    ttHH4.Scale(1/(ttHH4.Integral()))
    ttHH4.Draw('HIST SAME')
    ttHH4.SetAxisRange(0.,.51,'Y')
    ttH4.SetLineColor(ROOT.kAzure)
    ttH4.Scale(1/(ttH4.Integral()))
    ttH4.Draw('HIST SAME')
    ttZ4.SetLineColor(ROOT.kMagenta)
    ttZ4.Scale(1/(ttZ4.Integral()))
    ttZ4.Draw('HIST SAME')
    ttbb4.SetLineColor(ROOT.kGreen+2)
    ttbb4.Scale(1/(ttbb4.Integral()))
    ttbb4.Draw('HIST SAME')
    leg.Draw()

    c1.cd(5)####################################################### Jet muliplicity.
    ttHH5.SetLineColor(ROOT.kRed)
    ttHH5.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH5.SetStats(0)
    ttHH5.Scale(1/(ttHH5.Integral()))
    ttHH5.SetAxisRange(0.,.3,'Y')
    ttHH5.Draw('HIST SAME')
    ttH5.SetLineColor(ROOT.kAzure)
    ttH5.Scale(1/(ttH5.Integral()))
    ttH5.Draw('HIST SAME')
    ttZ5.SetLineColor(ROOT.kMagenta)
    ttZ5.Scale(1/(ttZ5.Integral()))
    ttZ5.Draw('HIST SAME')
    ttbb5.SetLineColor(ROOT.kGreen+2)
    ttbb5.Scale(1/(ttbb5.Integral()))
    ttbb5.Draw('HIST SAME')
    leg.Draw()

    c1.cd(6)############################################### Number of b-tagged jets.
    ttHH6.SetLineColor(ROOT.kRed)
    ttHH6.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH6.SetStats(0)
    ttHH6.Scale(1/(ttHH6.Integral()))
    ttHH6.SetAxisRange(0.,.40,'Y')
    ttHH6.Draw('HIST SAME')
    ttH6.SetLineColor(ROOT.kAzure)
    ttH6.Scale(1/(ttH6.Integral()))
    ttH6.Draw('HIST SAME')
    ttZ6.SetLineColor(ROOT.kMagenta)
    ttZ6.Scale(1/(ttZ6.Integral()))
    ttZ6.Draw('HIST SAME')
    ttbb6.SetLineColor(ROOT.kGreen+2)
    ttbb6.Scale(1/(ttbb6.Integral()))
    ttbb6.Draw('HIST SAME')
    leg.Draw()

    c2.cd(1).SetLogy() ################################################### Cut Flow.
    ttHH0.SetStats(0)
    ttHH0.SetFillColor(ROOT.kRed)
    cf.Add(ttHH0)
    cf.Draw()
    ttZ0.SetFillColor(ROOT.kMagenta)
    cf.Add(ttZ0)
    cf.Draw()
    ttH0.SetFillColor(ROOT.kAzure)
    cf.Add(ttH0)
    cf.Draw()
    ttbb0.SetFillColor(ROOT.kGreen+2)
    cf.Add(ttbb0)
    cf.Draw('HIST')
    leg.Draw()

    c2.cd(2) ############################################################# mT of the lepton and neutrino.
    ttHH7.SetLineColor(ROOT.kRed)
    ttHH7.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH7.SetStats(0)
    ttHH7.Scale(1/(ttHH7.Integral()))
    ttHH7.SetAxisRange(0.,.06,'Y')
    ttHH7.Draw('HIST SAME')
    ttH7.SetLineColor(ROOT.kAzure)
    ttH7.Scale(1/(ttH7.Integral()))
    ttH7.Draw('HIST SAME')
    ttZ7.SetLineColor(ROOT.kMagenta)
    ttZ7.Scale(1/(ttZ7.Integral()))
    ttZ7.Draw('HIST SAME')
    ttbb7.SetLineColor(ROOT.kGreen+2)
    ttbb7.Scale(1/(ttbb7.Integral()))
    ttbb7.Draw('HIST SAME')
    leg.Draw()

    c2.cd(3) ############################################################# pT of top two btag jets.
    ttHH8.SetLineColor(ROOT.kRed)
    ttHH8.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH8.SetStats(0)
    ttHH8.Scale(1/(ttHH8.Integral()))
    ttHH8.SetAxisRange(0.,.17,'Y')
    ttHH8.Draw('HIST SAME')
    ttH8.SetLineColor(ROOT.kAzure)
    ttH8.Scale(1/(ttH8.Integral()))
    ttH8.Draw('HIST SAME')
    ttZ8.SetLineColor(ROOT.kMagenta)
    ttZ8.Scale(1/(ttZ8.Integral()))
    ttZ8.Draw('HIST SAME')
    ttbb8.SetLineColor(ROOT.kGreen+2)
    ttbb8.Scale(1/(ttbb8.Integral()))
    ttbb8.Draw('HIST SAME')
    leg.Draw()

    c2.cd(4) ############################################################# Delta R of Btag and lepton
    ttHH9.SetLineColor(ROOT.kRed)
    ttHH9.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH9.SetStats(0)
    ttHH9.Scale(1/(ttHH9.Integral()))
    ttHH9.SetAxisRange(0.,0.06,'Y')
    ttHH9.Draw('HIST SAME')
    ttH9.SetLineColor(ROOT.kAzure)
    ttH9.Scale(1/(ttH9.Integral()))
    ttH9.Draw('HIST SAME')
    ttZ9.SetLineColor(ROOT.kMagenta)
    ttZ9.Scale(1/(ttZ9.Integral()))
    ttZ9.Draw('HIST SAME')
    ttbb9.SetLineColor(ROOT.kGreen+2)
    ttbb9.Scale(1/(ttbb9.Integral()))
    ttbb9.Draw('HIST SAME')
    leg.Draw()

    c2.cd(5) ############################################################# chi square of btag jets
    ttHH10.SetLineColor(ROOT.kRed)
    ttHH10.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH10.SetStats(0)
    ttHH10.Scale(1/(ttHH10.Integral()))
    ttHH10.SetAxisRange(0.,.4,'Y')
    ttHH10.Draw('HIST SAME')
    ttH10.SetLineColor(ROOT.kAzure)
    ttH10.Scale(1/(ttH10.Integral()))
    ttH10.Draw('HIST SAME')
    ttZ10.SetLineColor(ROOT.kMagenta)
    ttZ10.Scale(1/(ttZ10.Integral()))
    ttZ10.Draw('HIST SAME')
    ttbb10.SetLineColor(ROOT.kGreen+2)
    ttbb10.Scale(1/(ttbb10.Integral()))
    ttbb10.Draw('HIST SAME')
    leg.Draw()

    c2.cd(6) ############################################################# remaing pT
    ttHH11.SetLineColor(ROOT.kRed)
    ttHH11.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH11.SetStats(0)
    ttHH11.Scale(1/(ttHH11.Integral()))
    ttHH11.SetAxisRange(0.,.1,'Y')
    ttHH11.Draw('HIST SAME')
    ttH11.SetLineColor(ROOT.kAzure)
    ttH11.Scale(1/(ttH11.Integral()))
    ttH11.Draw('HIST SAME')
    ttZ11.SetLineColor(ROOT.kMagenta)
    ttZ11.Scale(1/(ttZ11.Integral()))
    ttZ11.Draw('HIST SAME')
    ttbb11.SetLineColor(ROOT.kGreen+2)
    ttbb11.Scale(1/(ttbb11.Integral()))
    ttbb11.Draw('HIST SAME')
    leg.Draw()

    c3.cd(1) ################################################### lowest delta R 
    ttHH12.SetLineColor(ROOT.kRed)
    ttHH12.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH12.SetStats(0)
    ttHH12.Scale(1/(ttHH12.Integral()))
    ttHH12.SetAxisRange(0.,.2,'Y')
    ttHH12.SetAxisRange(10.,125,'X')
    ttHH12.Draw('HIST SAME')
    ttH12.SetLineColor(ROOT.kAzure)
    ttH12.Scale(1/(ttH12.Integral()))
    ttH12.Draw('HIST SAME')
    ttZ12.SetLineColor(ROOT.kMagenta)
    ttZ12.Scale(1/(ttZ12.Integral()))
    ttZ12.Draw('HIST SAME')
    ttbb12.SetLineColor(ROOT.kGreen+2)
    ttbb12.Scale(1/(ttbb12.Integral()))
    ttbb12.Draw('HIST SAME')
    leg.Draw()

    c3.cd(2) ############################################################# lowest btag jets pT 
    ttHH13.SetLineColor(ROOT.kRed)
    ttHH13.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH13.SetStats(0)
    ttHH13.Scale(1/(ttHH13.Integral()))
    ttHH13.SetAxisRange(0.,.2,'Y')
    ttHH13.SetAxisRange(10.,140,'X')
    ttHH13.Draw('HIST SAME')
    ttH13.SetLineColor(ROOT.kAzure)
    ttH13.Scale(1/(ttH13.Integral()))
    ttH13.Draw('HIST SAME')
    ttZ13.SetLineColor(ROOT.kMagenta)
    ttZ13.Scale(1/(ttZ13.Integral()))
    ttZ13.Draw('HIST SAME')
    ttbb13.SetLineColor(ROOT.kGreen+2)
    ttbb13.Scale(1/(ttbb13.Integral()))
    ttbb13.Draw('HIST SAME')
    leg.Draw()

    c3.cd(3) ############################################################# lowest non btag jet pT
    ttHH14.SetLineColor(ROOT.kRed)
    ttHH14.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH14.SetStats(0)
    ttHH14.Scale(1/(ttHH14.Integral()))
    ttHH14.SetAxisRange(0.,1.05,'Y')
    ttHH14.SetAxisRange(10.,130,'X')
    ttHH14.Draw('HIST SAME')
    ttH14.SetLineColor(ROOT.kAzure)
    ttH14.Scale(1/(ttH14.Integral()))
    ttH14.Draw('HIST SAME')
    ttZ14.SetLineColor(ROOT.kMagenta)
    ttZ14.Scale(1/(ttZ14.Integral()))
    ttZ14.Draw('HIST SAME')
    ttbb14.SetLineColor(ROOT.kGreen+2)
    ttbb14.Scale(1/(ttbb14.Integral()))
    ttbb14.Draw('HIST SAME')
    leg.Draw()

    c3.cd(4) ############################################################# N/A
    ttHH15.SetLineColor(ROOT.kRed)
    ttHH15.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH15.SetStats(0)
    ttHH15.Scale(1/(ttHH15.Integral()))
    ttHH15.SetAxisRange(0.,1.05,'Y')
    ttHH15.SetAxisRange(10.,80,'X')
    ttHH15.Draw('HIST SAME')
    ttH15.SetLineColor(ROOT.kAzure)
    ttH15.Scale(1/(ttH15.Integral()))
    ttH15.Draw('HIST SAME')
    ttZ15.SetLineColor(ROOT.kMagenta)
    # ttZ15.Scale(1/(ttZ15.Integral()))
    ttZ15.Draw('HIST SAME')
    ttbb15.SetLineColor(ROOT.kGreen+2)
    ttbb15.Scale(1/(ttbb15.Integral()))
    ttbb15.Draw('HIST SAME')
    leg.Draw()

    c3.cd(5) ############################################################# N/A
    ttHH16.SetLineColor(ROOT.kRed+1)
    ttHH16.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH16.SetStats(0)
    ttHH16.Scale(1/(ttHH16.Integral()))
    ttHH16.SetAxisRange(1.0e+4,1.0e+8,'X')
    ttHH16.Draw('HIST SAME')
    ttH16.SetLineColor(ROOT.kAzure)
    ttH16.Scale(1/(ttH16.Integral()))
    ttH16.Draw('HIST SAME')
    ttZ16.SetLineColor(ROOT.kMagenta)
    ttZ16.Scale(1/(ttZ16.Integral()))
    ttZ16.Draw('HIST SAME')
    ttbb16.SetLineColor(ROOT.kGreen+2)
    ttbb16.SetFillStyle(1001)
    ttbb16.Scale(1/(ttbb16.Integral()))
    ttbb16.Draw('HIST SAME')
    leg.Draw()

    c3.cd(6) ############################################################# N/A
    ttHH17.SetLineColor(ROOT.kRed)
    ttHH17.SetFillColorAlpha(ROOT.kRed-10,0)
    ttHH17.SetStats(0)
    ttHH17.Scale(1/(ttHH17.Integral()))
    ttHH17.SetAxisRange(0.0,1.0e+7,'X')
    ttHH17.SetAxisRange(0.,.7,'Y')
    ttHH17.Draw('HIST SAME')
    ttH17.SetLineColor(ROOT.kAzure)
    ttH17.Scale(1/(ttH17.Integral()))
    ttH17.Draw('HIST SAME')
    ttZ17.SetLineColor(ROOT.kMagenta)
    ttZ17.Scale(1/(ttZ17.Integral()))
    ttZ17.Draw('HIST SAME')
    ttbb17.SetLineColor(ROOT.kGreen+2)
    ttbb17.Scale(1/(ttbb17.Integral()))
    ttbb17.Draw('HIST SAME')
    leg.Draw()
#! /usr/bin/env python
import os
import glob
import math

import ROOT
# Import stuff from FWLite
import sys
from DataFormats.FWLite import Events, Handle


files = ['out_reco.root']

# Create the output file. 
f = ROOT.TFile("out_hist.root", "recreate")
f.cd()

muonPtHist = ROOT.TH1F('muonPtHist', 'Muon p_{T}', 300, 0., 600.)

events = Events (files)

muonHandle         = Handle( "std::vector<reco::Track>" )
muonLabel = ("standAloneMuons","","RECO")

# loop over events
count = 0
ntotal = events.size()
for event in events:
  count = count + 1

  event.getByLabel( muonLabel, muonHandle )
  muons = muonHandle.product()

  for imuon in range( 0, len( muons ) ) :
    muonPtHist.Fill( muons[imuon].pt() )


muonPtHist.GetXaxis().SetTitle("standAloneMuons (GeV)")

f.cd()
f.Write()
f.Close()


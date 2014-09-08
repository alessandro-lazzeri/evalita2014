CORPUS = tweet

# ----------------------------------------------------------------------
# programs

TANLDIR = /project/piqasso/QA/Tanl
TANLBIN = $(TANLDIR)/bin

# ----------------------------------------------------------------------
# Tanl Tools and models

SENTSPLITTER =  $(TANLBIN)/Splitta.py
SENTSPLITTER_MODEL = $(TANLDIR)/data/split/sentence/italian.splitta
TOKENIZER =	$(TANLDIR)/src/split/Tokenizer/tw_lexer_it

# Tokenize the tagged clinical records
# Patch for bug in Splitta which stops when finding line ending with '\':
# sided hearing loss. \
#
$(CORPUS).tok: $(CORPUS).txt $(SENTSPLITTER) $(SENTSPLITTER_MODEL) $(TOKENIZER)
	sed 's/\\$$//' $< |\
	$(SENTSPLITTER) $(SENTSPLITTER_MODEL) 2> /dev/null |\
	$(TOKENIZER) > $@

$(CORPUS).sent: $(CORPUS).txt $(SENTSPLITTER) $(SENTSPLITTER_MODEL) $(TOKENIZER)
	sed 's/\\$$//' $< |\
	$(SENTSPLITTER) $(SENTSPLITTER_MODEL) 2> /dev/null > $@

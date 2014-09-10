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

# Tokenize the tweets and recombine.
# First add newline to separate each tweet and remove extra \ in front of / and ". FIXME: who adds them to tweets?
# After combine back tokens into a single line, space separated
#
$(CORPUS).tok: $(CORPUS).txt $(SENTSPLITTER) $(SENTSPLITTER_MODEL) $(TOKENIZER)
	sed -e '/$$/G' -e 's:\\/:/:g' $< |\
	$(SENTSPLITTER) $(SENTSPLITTER_MODEL) 2> /dev/null |\
	$(TOKENIZER) |\
	sed -e ':a N;/\n$$/P;/\n$$/d;s/\n/ /;ta' > $@

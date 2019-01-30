# PyTorch Pretrained Bert Annotation

> This BERT annotation repo is for my personal study.

The raw README of PyTorch Pretrained Bert is [here](README_bert.md).

## Arch

The BertModel and BertForMaskedLM arch.

#### BertModel Arch
   - BertEmbeddings
      - word_embeddings: Embedding(30522, 768)
      - position_embeddings: Embedding(512, 768)
      - token_type_embeddings: Embedding(2, 768)
      - LayerNorm: BertLayerNorm()
      - dropout: Dropout(p=0.1)
   - BertEncoder
      - BertLayer: (12 layers)
         - BertAttention
            - BertSelfAttention
               - query: Linear(in_features=768, out_features=768, bias=True)
               - key: Linear(in_features=768, out_features=768, bias=True)
               - value: Linear(in_features=768, out_features=768, bias=True)
               - dropout: Dropout(p=0.1)
            - BertSelfOutput
               - dense: Linear(in_features=768, out_features=768, bias=True)
               - LayerNorm: BertLayerNorm()
               - dropout: Dropout(p=0.1)
         - BertIntermediate
            - dense: Linear(in_features=768, out_features=3072, bias=True)
            - activation: gelu
         - BertOutput
            - dense: Linear(in_features=3072, out_features=768, bias=True)
            - LayerNorm: BertLayerNorm()
            - dropout: Dropout(p=0.1)
   - BertPooler
      - dense: Linear(in_features=768, out_features=768, bias=True)
      - activation: Tanh()

#### BertForMaskedLM Arch
   - BertModel
      - BertEmbeddings
         - word_embeddings: Embedding(30522, 768)
         - position_embeddings: Embedding(512, 768)
         - token_type_embeddings: Embedding(2, 768)
         - LayerNorm: BertLayerNorm()
         - dropout: Dropout(p=0.1)
      - BertEncoder
         - BertLayer: (12 layers)
            - BertAttention
               - BertSelfAttention
                  - query: Linear(in_features=768, out_features=768, bias=True)
                  - key: Linear(in_features=768, out_features=768, bias=True)
                  - value: Linear(in_features=768, out_features=768, bias=True)
                  - dropout: Dropout(p=0.1)
               - BertSelfOutput
                  - dense: Linear(in_features=768, out_features=768, bias=True)
                  - LayerNorm: BertLayerNorm()
                  - dropout: Dropout(p=0.1)
            - BertIntermediate
               - dense: Linear(in_features=768, out_features=3072, bias=True)
               - activation: gelu
            - BertOutput
               - dense: Linear(in_features=3072, out_features=768, bias=True)
               - LayerNorm: BertLayerNorm()
               - dropout: Dropout(p=0.1)
      - BertPooler
         - dense: Linear(in_features=768, out_features=768, bias=True)
         - activation: Tanh()
   - BertOnlyMLMHead
      - BertLMPredictionHead
         - transform: BertPredictionHeadTransform
            - dense: Linear(in_features=768, out_features=768, bias=True)
            - LayerNorm: BertLayerNorm()
         - decoder: Linear(in_features=768, out_features=30522, bias=False)
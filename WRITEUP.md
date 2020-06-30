# Project Write-Up


## Explaining Custom Layers

- process behind converting custom layers 

Adding extensions to both model optmizer and IE 
To make registered custom layers we need to follow this :
https://github.com/david-drew/OpenVINO-Custom-Layers/blob/master/2019.r2.0/ReadMe.Linux.2019.r2.md


- potential reasons for handling custom layers 
Without handling it we cannot convert specific models to IR
Model optmizers should need to handle unsupported layers 




## Comparing Model Performance

My method(s) to compare models before and after conversion to Intermediate Representations
were...

The difference between model accuracy pre- and post-conversion was...
    preconversion-model < post-conversion model

The size of the model pre- and post-conversion was...
    preconversion-model -69MB  post-conversion model-67 MB
The inference time of the model pre- and post-conversion was...
    preconversion-model -avg infer time - 124.2ms
    post-conversion model -avg infer time - 4.78ms 
## Assess Model Use Cases

Some of the potential use cases of the people counter app are...
    1. Better queue management in retail shops 
    2. Products that customers like higher in a mall 
    3. Periodic usage of a certain asset 

Each of these use cases would be useful because...
    1. it would increase the profit for the user
    2. Identify customers preference
    3. regulated access 
    
    
## Assess Effects on End User Needs

Lighting, model accuracy, and camera focal length/image size have different effects on a
deployed edge model. The potential effects of each of these are as follows...

Lighting - We need input image with proper lighting because we cant identify anything in a black image
model accuracy - We need to give true results not faulty results 
camera focal length - it can be wider or narrower and it depends on the requirment 
Image size - Greater the resolution higher the accuracy of prediction but it will take higher time for 
inference 

## Model Research

[This heading is only required if a suitable model was not found after trying out at least three
different models. However, you may also use this heading to detail how you converted 
a successful model.]

In investigating potential people counter models, I tried each of the following three models:

- Model 1: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...
  
- Model 2: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...

- Model 3: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...

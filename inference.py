#!/usr/bin/env python3
"""
 Copyright (c) 2018 Intel Corporation.

 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
 the following conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from openvino.inference_engine import IENetwork, IECore


class Network:
    """
    Load and configure inference plugins for the specified target devices
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        ### TODO: Initialize any class variables desired ###
        self.plugNetwork = IECore()
        self.execNetwork = None
        self.network = None
        self.inputLayer = None



    def load_model(self, xml_path, numRequests, device_name, cpu_extension):

        self.network = IENetwork(model=xml_path,weights=xml_path.split(".")[0]+".bin")
        suppLayers = self.plugNetwork.query_network(network=self.network,device_name=device_name)
        unsuppLayers = [k for k in self.network.layers.keys() if k not in suppLayers]

        if len(unsuppLayers)!=0:
            if not cpu_extension == None :
                self.plugNetwork.add_extension(cpu_extension,device_name)
                suppLayers = self.plugNetwork.query_network(network=self.network,device_name=device_name)
                unsuppLayers = [k for k in self.network.layers.keys() if k not in suppLayers]
                if len(unsuppLayers)!=0:
                    exit(1)
            else:
                exit(1)


        self.execNetwork = self.plugNetwork.load_network(network=self.network,num_requests=numRequests,device_name=device_name)


        self.inputLayer = next(iter(self.network.inputs))
        return

    def get_input_shape(self):

        return self.network.inputs[self.inputLayer].shape


    def exec_net(self, frame, req_id):

        self.execNetwork.start_async(request_id=req_id,inputs={self.inputLayer:frame})
        return

    def wait(self, req_id):

        return self.execNetwork.requests[req_id].wait(-1)


    def get_output(self, req_id):

        outputResults = self.execNetwork.requests[req_id].outputs
        return [outputResults[k] for k in outputResults.keys()]




import VectorSource from "ol/source/Vector";
import React from "react";
import {
  adjacencyMatrixToLineFeature,
  nodesToPointsFeature,
} from "../../util/OpenLayersFeatures";

const FileInput = (props) => {
  const { setAdjMatrix, setNodes, featuresLayerRef } = props;

  const fileValid = (nodes, adj) => {
    const nodesCount = nodes.length;

    var matrixValid = true;

    adj.forEach((row) => {
      matrixValid = matrixValid && row.length == nodesCount;
    });

    return nodesCount == adj.length && matrixValid;
  };
  const parseFile = async (e) => {
    e.preventDefault();
    const reader = new FileReader();

    console.log("read file");

    reader.onload = async (e) => {
      try {
        const text = e.target.result;

        const input = JSON.parse(text);
        const { adj: inputAdj, nodes: inputNodes } = input;

        console.log(fileValid(inputNodes, inputAdj));

        if (fileValid(inputNodes, inputAdj)) {
          setAdjMatrix(inputAdj);
          setNodes(inputNodes);

          const lineFeatures = adjacencyMatrixToLineFeature(
            inputAdj,
            inputNodes
          );
          const pointFeatures = nodesToPointsFeature(inputNodes);
          const features = [...lineFeatures, ...pointFeatures];

          featuresLayerRef.current.setSource(
            new VectorSource({
              features: features,
            })
          );
        } else {
          alert("Please input the correct json format");
        }
      } catch (err) {
        console.log(err);
        alert("Please input the correct json format");
      }
    };

    reader.readAsText(e.target.files[0]);
  };
  return (
    <div>
      <div className="d-flex text-center mb-4">
        <h3 className="file-input-title w-100">File Input</h3>
      </div>
      <input type="file" onChange={(e) => parseFile(e)} />
      <style>
        {`
                    .file-input-title {
                        background: #B98389;
                        color: #E4DBD9;
                        padding: .5rem 0rem;
                        border-radius: 7px;                
                    }
                `}
      </style>
    </div>
  );
};

export default FileInput;

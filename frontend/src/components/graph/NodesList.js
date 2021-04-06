import React from "react";

const NodesList = (props) => {
  const { nodes, handleDeleteNodeAtIndex } = props;

  return (
    <>
      <div>
        <h3 className="mb-4 node-list-title text-center">Node List</h3>
        {nodes.map((node, index) => {
          return (
            <div
              key={index}
              className="node-list-element d-flex align-items-center mb-3"
            >
              <button
                onClick={() => handleDeleteNodeAtIndex(index)}
                className="x-btn mr-4"
              >
                X
              </button>
              <p className="m-0 node-el">{`${node.name}| ${node.longitude}, ${node.latitude}`}</p>
            </div>
          );
        })}
      </div>
      <style>
        {`
            .x-btn {
                background: #D36582;
                color: white;
                border: none;
                border-radius: 3px;
                padding: .5rem 1.5rem;
            }

            .x-btn:focus {
                outline: none;
                border: none;
            }

            .node-el {
                background: #e4dbd9;
                padding: .5rem 1.5rem;
                border-radius: 4px;
            }

            .node-list-title {
                background: #B98389;
                color: #E4DBD9;
                padding: .5rem 1rem;
                border-radius: 7px; 
            }
          `}
      </style>
    </>
  );
};

export default NodesList;

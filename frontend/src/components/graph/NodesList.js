import React from "react";

const NodesList = (props) => {
  const { nodes, handleDeleteNodeAtIndex } = props;

  return (
    <>
      <div>
        {/* {console.log(nodes)} */}
        {nodes.map((node, index) => {
          return (
            <div
              key={index}
              className="node-list-element"
              style={{ display: "flex" }}
            >
              <button onClick={() => handleDeleteNodeAtIndex(index)}>
                Delete
              </button>
              <p>{`${node.name}. Longitude: ${node.longitude} | Latitude: ${node.latitude}`}</p>
            </div>
          );
        })}
      </div>
      <style>
        {`
    .node-list-element {
        display: flex;
    }
          `}
      </style>
    </>
  );
};

export default NodesList;

import { Modal, Button } from 'react-bootstrap';
import React from 'react';

function ViewModal( { isOpen, closeModal, selectedRowData } ) {
    return (
        <Modal show={isOpen} onHide={closeModal}>
            <Modal.Header closeButton>
                <Modal.Title>Analize pilots</Modal.Title>
            </Modal.Header>
            <Modal.Body> 
                <h2>Dettagli del pilota selezionato</h2>
                <p>Name: {selectedRowData.name}</p>
                <p>Team: {selectedRowData.team}</p>
                <p>GpWin: {selectedRowData.gpWin}</p>
                <p>GpMade: {selectedRowData.gpMade}</p>
                <p>Podiums: {selectedRowData.podiums}</p>
                <p>Points: {selectedRowData.points}</p>
                <p>FastestLaps: {selectedRowData.fastLaps}</p>
                </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={closeModal}>
                    Close
                </Button>
                
            </Modal.Footer>
        </Modal>);
};

export default ViewModal;
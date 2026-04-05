import numpy as np
from sklearn.decomposition import PCA
from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap
from qiskit_aer.primitives import Sampler


class QuantumRecommender:
    def __init__(self):
        self.n_qubits = 4
        self.pca = PCA(n_components=self.n_qubits)
        self.feature_map = ZZFeatureMap(
            feature_dimension=self.n_qubits,
            reps=2,
            entanglement="linear"
        )
        self.sampler = Sampler()
        self.is_fitted = False

    def fit_transform_data(self, vectors):
        reduced = self.pca.fit_transform(vectors)
        self.is_fitted = True
        return reduced

    def transform_single(self, vector):
        if not self.is_fitted:
            raise RuntimeError("Quantum PCA not fitted")
        return self.pca.transform(vector.reshape(1, -1))

    def compute_quantum_similarity(self, vec_a, vec_b):
        try:
            qc = QuantumCircuit(self.n_qubits)

            qc.append(self.feature_map.bind_parameters(vec_a), range(self.n_qubits))
            qc.append(self.feature_map.bind_parameters(vec_b).inverse(), range(self.n_qubits))

            qc.measure_all()

            result = self.sampler.run(qc).result()
            quasi_dist = result.quasi_dists[0]

            return quasi_dist.get(0, 0.0)

        except Exception as e:
            print("Quantum Engine Error:", e)
            return 0.0

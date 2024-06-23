class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        bank = set(bank)
        if endGene not in bank:
            return -1

        cnt_step = 0
        queue = deque([startGene])
        while queue:
            cnt_step += 1
            for _ in range(len(queue)):
                cur_gene = queue.popleft()
                for i in range(len(cur_gene)):
                    for c in 'ACGT':
                        if c == cur_gene[i]:
                            continue
                        new_gene = cur_gene[:i] + c + cur_gene[i + 1:]
                        if new_gene == endGene:
                            return cnt_step
                        if new_gene in bank:
                            bank.remove(new_gene)
                            queue.append(new_gene)
        return -1
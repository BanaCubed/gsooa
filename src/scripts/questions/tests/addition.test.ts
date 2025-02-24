import { describe, expect, test } from 'vitest';
import Addition from '../addition';

describe('Correct Addition values', () => {
    test('Correct type value', () => {
        expect(new Addition(1, 1).type).to.eq(0);
    });

    test('Correct answer value', () => {
        for (let i = 0; i < 20; i++) {
            const question = new Addition(Math.floor(Math.random() * 9 + 1), Math.random());
            let answer = 0;
            for (let j = 0; j < question.variables.length; j++) {
                answer += question.variables[j];
            }
            expect(question.answer[0]).to.eq(answer);
        }
    });
});

describe('Error throwing', () => {
    test('Level -1 - Should error', () => {
        expect(() => new Addition(-1, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Addition" has a minimum level of "1", whereas the current level is "-1"]`,
        );
    });
    test('Level 0 - Should error', () => {
        expect(() => new Addition(0, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Addition" has a minimum level of "1", whereas the current level is "0"]`,
        );
    });

    test('Level 1 - Should not error', () => {
        expect(() => new Addition(1, 77)).not.toThrowError();
    });
    test('Level 2 - Should not error', () => {
        expect(() => new Addition(2, 77)).not.toThrowError();
    });

    test('Level 9 - Should not error', () => {
        expect(() => new Addition(9, 77)).not.toThrowError();
    });
    test('Level 10 - Should not error', () => {
        expect(() => new Addition(10, 77)).not.toThrowError();
    });
    
    test('Level 11 - Should error', () => {
        expect(() => new Addition(11, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Addition" has a maximum level of "1", whereas the current level is "11"]`,
        );
    });
    test('Level 12 - Should error', () => {
        expect(() => new Addition(12, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Addition" has a maximum level of "1", whereas the current level is "12"]`,
        );
    });
});
